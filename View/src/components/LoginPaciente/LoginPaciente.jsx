import React, { useState } from 'react';
import axios from 'axios';
import "./LoginPaciente.css"

function LoginPaciente() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleLogin = async () => {
        try {
            const response = await axios.post('sua-url-da-api/login', {
                username: username,
                password: password
            });

            // Lógica de autenticação bem-sucedida, como salvar o token de autenticação no estado global ou nos cookies
            console.log('Login bem-sucedido!', response.data);
        } catch (error) {
            // Lógica de tratamento de erro
            console.error('Erro ao fazer login:', error);
            setError('Usuário ou senha incorretos');
        }
    };

    return (
        <div className='login-container-paciente'>
            
            <div className='loginData'>
                
                {error && <p>{error}</p>}
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
