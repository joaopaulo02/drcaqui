import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Importando o hook useNavigate
import "./LoginPaciente.css";
import ChatBot from '../../Components/ChatBot/ChatBot';

function LoginPaciente() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate(); // Inicializando o hook useNavigate

    const handleLogin = () => {
        // Simplesmente navega para a próxima página
        navigate('/'); // Redireciona para a próxima página
    };

    return (
        <div className='login-container-paciente'>
            <ChatBot />
            <div className='loginData'>
                <form className="loginForm" onSubmit={(e) => {
                    e.preventDefault();
                    handleLogin();
                }}>
                    <h2>Login</h2> 
                    <label>Usuário:</label>
                    <input className='input-component'
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                
                    <label>Senha:</label>
                    <input className='input-component'
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />

                    <button type="submit" className='button-component'>Entrar</button>
                </form>
            </div>
            <div className='imgleft-paciente'>
            </div>
        </div>
    );
}

export default LoginPaciente;
