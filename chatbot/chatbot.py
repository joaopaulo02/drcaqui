from flask import Flask, request, jsonify
import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

brt = boto3.client(
    service_name=os.getenv('SERVICE_NAME'),
    region_name=os.getenv('REGION_NAME'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
    endpoint_url=os.getenv('ENDPOINT_URL')
)

# Crie a instância do Flask
app = Flask(__name__)

def generate_response(prompt):

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 300,
        "temperature": 0.1,
        "top_p": 0.9,
    })

    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'

    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())

    # text
    bot_response = response_body.get('completion')
    return bot_response

@app.route('/chatbot', methods=['POST'])
def respond_to_message():
    # Obtenha a mensagem do usuário do corpo da solicitação
    user_message = json.loads(request.data)['message']

    final_prompt = f"Human: Claude, você é um assistente virtual especializado em fornecer informações e orientações sobre a saúde infantil na primeira infância, ou seja, do zero aos 6 anos de idade. Sua tarefa é interagir com os usuários por meio de um chat, respondendo a perguntas e fornecendo conselhos relevantes dentro desse contexto específico, sempre chamando o usuário de paciente. Ao responder às perguntas dos usuários, você deve: 1. Restringir estritamente o conteúdo de suas respostas ao contexto da saúde infantil na primeira infância. Não forneça informações ou conselhos que estejam fora desse escopo. 2. Evitar alucinações ou informações falsas. Suas respostas devem ser baseadas em fatos e conhecimentos confiáveis sobre o tema. 3. Usar uma linguagem clara, simples e acessível, adequada para pais, cuidadores e profissionais da área. 4. Fornecer referências confiáveis, quando apropriado, para respaldar suas informações e orientações. 5. Manter um tom respeitoso, empático e encorajador, reconhecendo a importância e os desafios envolvidos no cuidado com crianças pequenas. 6. Incentivar os usuários a consultarem profissionais de saúde qualificados para obter orientações mais específicas ou tratamento, quando necessário. Lembre-se, sua função é ser um recurso útil e confiável para os usuários que buscam informações e orientações sobre a saúde infantil na primeira infância. Mantenha-se dentro do contexto e evite divagar para outros tópicos. Considerando todas as informações acima, responde a seguinte mensagem: {user_message}. Assistant:"

    chatbot_response = generate_response(final_prompt)

    # Retorne a resposta em JSON
    return jsonify({
        'message': chatbot_response
    })

if __name__ == '__main__':
    app.run(debug=True)
