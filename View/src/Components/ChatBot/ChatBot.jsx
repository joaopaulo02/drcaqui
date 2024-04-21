import React, { useState } from 'react';
import "./ChatBot.css";

const ChatBot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [chatMessages, setChatMessages] = useState([
    { type: 'incoming', text: 'Olá, sou Dr. Caqui! Como posso te ajudar?' }
  ]);
  const [inputValue, setInputValue] = useState('');

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const sendMessage = async () => {
    if (inputValue.trim() === '') return;

    // Envia a mensagem para a API
    try {
      const response = await fetch('sua_url_da_api', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: inputValue })
      });
      const data = await response.json();
      
      // Adiciona a mensagem enviada pelo usuário
      setChatMessages(prevMessages => [
        ...prevMessages,
        { type: 'outgoing', text: inputValue }
      ]);

      // Adiciona a resposta da API
      setChatMessages(prevMessages => [
        ...prevMessages,
        { type: 'incoming', text: data.response }
      ]);

      // Limpa o campo de entrada
      setInputValue('');
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
    }
  };

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  return (
    <div className={isOpen ? 'show-chatbot' : ''}>
      <button className="chatbot-toggler" onClick={toggleChat}>
        <span className='material-symbols-outlined'>
          {isOpen ? 'close' : 'send'}
        </span>
      </button>
      <div className={`chatbot ${isOpen ? 'open' : ''}`}>
        <header>
          <h2>Chatbot</h2>
          <span className='material-symbols-outlined' onClick={toggleChat}>
            close
          </span>
        </header>
        <ul className='chatbox'>
          {chatMessages.map((message, index) => (
            <li key={index} className={`chat ${message.type}`}>
              <p>{message.text}</p>
            </li>
          ))}
        </ul>
        <div className="chat-input">
          <textarea
            placeholder='Digite a mensagem'
            value={inputValue}
            onChange={handleInputChange}
            required
          ></textarea>
          <span className='material-symbols-outlined' onClick={sendMessage}>
            send
          </span>
        </div>
      </div>
    </div>
  );
};

export default ChatBot;
