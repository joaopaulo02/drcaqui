import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Importe o hook useNavigate
import "./Login.css";

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate(); // Inicialize o hook useNavigate

    const handleLogin = () => {
        navigate('/'); // Redirecionar para a próxima página após o envio do formulário
    };

    return (
        <div className='login-container'>
            <div className='imgleft'>
            </div>
            <div className='loginData'>
                <form className="loginForm" onSubmit={(e) => {
                    e.preventDefault();
                    handleLogin();
                }}>
                    <h2 className='title-doctor'>Login</h2> 
                    <label>Usuário:</label>
                    <input className='input-component'
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                    <label>Senha:</label>
                    <input className='input-component'
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                    <button type="submit" className='button-component'>Entrar</button>
                </form>
            </div>
        </div>
    );
}

export default Login;
