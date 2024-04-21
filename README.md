# Documentação - Doutor Caqui

<h2>Descrição da Aplicação:</h2>

<h3> O Doutor Caqui é um aplicativo web completo para auxiliar no acompanhamento da saúde na primeira infância. A aplicação possui três camadas principais: </h3>
<br>
<ol>
    <li>
    Backend Flask:

    Utiliza a API do Amazon Bedrock e o modelo Claude V2 para processar perguntas em linguagem natural e retornar respostas relevantes em formato JSON.
    Funciona como uma API REST, permitindo a integração com outros sistemas.
   ![api_ref](https://media.discordapp.net/attachments/733037083941142681/1231560480695521330/api_ref.png?ex=66376713&is=6624f213&hm=46cd7625821a5a4e176a4ac0beffcc17e7d4b0c19dd8a0be940641fb90aeb7f1&=&format=webp&quality=lossless&width=704&height=722)
</li>
<li>
    Backend C#:
    
    Registra e armazena dados cadastrados dos usuários em um banco de dados MySQL.
    Inclui informações essenciais para a saúde da criança, como peso, altura, informações de vacinação, etc.
    Retorna os dados cadastrados em formato JSON para consulta e análise.
   ![db_c#](https://media.discordapp.net/attachments/733037083941142681/1231560516862738442/db_c.jpg?ex=6637671c&is=6624f21c&hm=3efa8e3bc75eedaa656ca778d99110bd5a000873a29a51df51dd89b1030220b2&=&format=webp&width=734&height=722)
</li>
<br>
<li>
4. Frontend React:

    Consome a API Flask para alimentar o chatbot Doutor Caqui.
    Permite que os usuários interajam com o chatbot de forma natural e façam perguntas sobre a saúde da primeira infância.
    Exibe as respostas do chatbot em formato amigável e informativo.
    Consome os dados JSON gerados pelo backend C# para fornecer informações adicionais sobre a saúde da criança.
   ![chatbot_img](https://media.discordapp.net/attachments/733037083941142681/1231560480984793139/chatbot-img.png?ex=66264393&is=6624f213&hm=835a4bab2b8c177df86c6c045e150b3596c5d906043bdca024e966fcbbeb37a2&=&format=webp&quality=lossless)
</li>
</ol>
<br>
<h2> Funcionalidades do Doutor Caqui: </h2>
<ul>
    <li>
    Chatbot:
        Responde perguntas sobre saúde na primeira infância de forma abrangente e informativa.
        Utiliza linguagem natural para facilitar a interação com os usuários.
        Adapta suas respostas de acordo com a idade da criança e o contexto da conversa.
     </li>
    <li>
    Banco de Dados:
        Armazena dados essenciais para a saúde da criança, como peso, altura, informações de vacinação, etc.
        Permite o acompanhamento do desenvolvimento da criança ao longo do tempo.
        Facilita a geração de relatórios e análises sobre a saúde da criança.
    </li>
    <li>
    Integração:
        A API REST do backend Flask permite a integração com outros sistemas, como prontuários eletrônicos de saúde.
        O frontend React pode ser personalizado para atender às necessidades específicas de diferentes usuários. 
    </li>
</ul>
<br>
<h2>Benefícios do Doutor Caqui: </h2>

    - Melhora o acesso à informação:
        Permite que os pais e responsáveis ​​tenham acesso a informações confiáveis ​​sobre a saúde da primeira infância de forma prática e acessível.
        Reduz a necessidade de consultas médicas desnecessárias.
    Promove a saúde da criança:
        Auxilia no acompanhamento do desenvolvimento da criança e na identificação de possíveis problemas de saúde.
        Incentiva a adoção de hábitos saudáveis ​​para as crianças.
    Empodera os pais e responsáveis:
        Fornece as ferramentas necessárias para que os pais e responsáveis ​​tomem decisões informadas sobre a saúde de seus filhos.
        Reduz a ansiedade e o estresse relacionados à saúde da criança.

Tecnologias Utilizadas:

    Backend Python:
        Linguagem de programação: Python
        Framework: Flask
        API: Amazon Bedrock
        Modelo de linguagem: Claude V2
    Backend C#:
        Linguagem de programação: C#
        Framework: Microsoft.EntityFrameworkCore
        Banco de dados: MySQL
    Frontend:
        Biblioteca JavaScript: React

Implementação:

A implementação do Doutor Caqui envolve o desenvolvimento de três componentes principais:

    Backend Flask:
        Implementar a API REST para processar perguntas e retornar respostas em formato JSON.
        Integrar a API do Amazon Bedrock e o modelo Claude V2 para processamento de linguagem natural.

    Backend C#:
        Desenvolver a aplicação C# para registro e armazenamento de dados no banco de dados MySQL.
        Criar APIs para consulta e recuperação de dados do banco de dados em formato JSON.

    Frontend React:
        Desenvolver a interface do usuário React para interação com o chatbot Doutor Caqui.
        Consumir a API Flask para obter respostas do chatbot.
        Consumir os dados JSON do backend C# para exibir informações adicionais sobre a saúde da criança.

Testes:

A aplicação Doutor Caqui deve ser testada rigorosamente para garantir seu funcionamento correto e confiável. Os testes devem incluir:

    Testes unitários:
        Testar cada componente da aplicação individualmente.
    Testes de integração:
        Testar a interação entre os diferentes componentes da aplicação.
    Testes de aceitação:
        Testar a aplicação do ponto de vista do usuário.
