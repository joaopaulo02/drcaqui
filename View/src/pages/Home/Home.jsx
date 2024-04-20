import React from 'react';
import "./Home.css";
import { Link } from 'react-router-dom';


const Home = () => {
    return (
        <div>
            <div className='welcomeHome'>
                <h1>Seja Bem vindo!</h1>
                <div className='welcomeHomeComponents'> 
                    <Link to="/loginPaciente" className='welcomeHomeComponents-item' style={{ textDecoration: 'none', color: 'black' }}>
                        <div className='welcomeHomeComponents-component'>
                            <img src="dr.bebe.svg" alt="doutor caqui bebe" className='componentsHomeImgs' />
                            <h2>Paciente</h2>
                        </div>
                    </Link>
                    <Link to="/loginDoutor" className='welcomeHomeComponents-item' style={{ textDecoration: 'none', color: 'black' }}>
                        <div className='welcomeHomeComponents-component'>
                            <img src="dr..svg" alt="doutor caqui medico" className='componentsHomeImgs'/>
                            <h2>Profissional</h2>
                        </div>
                    </Link>
                </div>
            </div>
        </div>

    );
}

export default Home;
