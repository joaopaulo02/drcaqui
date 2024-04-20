from flask import Flask, request, jsonify
import boto3
import json

brt = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1',
    aws_access_key_id='ASIA4MTWHZPHBRQ4GQCB',
    aws_secret_access_key='INuPCUsYPtTTZ+OezROL5JFzMNNoaJV3csUVNVft',
    aws_session_token='IQoJb3JpZ2luX2VjEOr//////////wEaCXVzLWVhc3QtMSJHMEUCIQDYBACE395SebzaO31EJqTKdfA4dns06oGGq0o6/jUlSQIgMRSg31QlHqOEhwne8L4hirSgx5DiR2Qpygd1/eUXD5oqiwMIMxAAGgw4NTE3MjUyNDEyOTQiDIDI2bt1SDwTAGLyoyroAnGrk9Iooa/RTWaTpPtT1H6EJwa5CT8HMgMud0zYKwFazya77lNRmD/9KJe43ugbpYQUmpfE9Ird1qBBG0NzgxXptad8BjCl/weLLZZfrXQwhKT8SdaY+RBXRrm4UHq/j6WQfMdfyPKoa/pz20strq9EH+wYpXkKDTAbjGfUqWz6beGlND647qjZxB4THum6GHQNgxNMgKRyuELEFGWAAex2cjIhFkij8ZFAXPD8E+6qr0TiIZ+VnPh9hKPFIpHcHUJQq7smWIvY0ws+e+dtk2Bd37WDcq4tZ3q7TqjJ5p1IBb4sod/goKH0dn60Hlq/QlGI3zmd+QcDfe5PrTCwb3lOlfFxvr9UpSZY/KBqHmtgvUostJcSr7XK8deOZ7D2sQ8TO8dcFBqKFMnbUM7r9oMMMSo5BZfLCXRLoYf83CDDZgMb7ZzYdDxq9uPZMvkPm9OclG41LMzMh5MT8QjUheAiDJZL6oBtqzC984+xBjqmAaN0C2uPH7XnDncOccZIQdp244fkllRJLFaYIEHJfNvhubjo0AZZeddTJ6cVa+TOPVt3jZwqnbGApjmS6i2Yx5PyIRY/tNmUPZ41NuIXYwDaZSTNdf6mLfe6wWg8DNSJ4v40Wp2kraC267bW9Sl7CMvDsBzLW/+Tbzkbyx+i3rDpLJAiYO2fC6pwKu1HEygF+Vb1gbS8Ds2z1y/UBC/bIgfV6CLXPAo=',
    endpoint_url='https://bedrock-runtime.us-east-1.amazonaws.com'
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
