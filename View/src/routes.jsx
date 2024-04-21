import React from "react";
import { Route, BrowserRouter, Routes } from "react-router-dom"; // Importe também o componente <Routes>
import Home from "./pages/Home/Home.jsx";
import Sobre from "./pages/Sobre/Sobre.jsx";
import Usuario from "./pages/Usuario/Usuario.jsx";
import Login from "./pages/LoginDoutor/Login.jsx";
import LoginPaciente from "./pages/LoginPaciente/LoginPaciente.jsx";

const AppRoutes = () => {
   return(
       <BrowserRouter>
           <Routes> {/* Envolver os componentes <Route> dentro de <Routes> */}
               <Route path="/" element={<Home />} exact />
               <Route path="/sobre" element={<Sobre />} />
               <Route path="/usuario" element={<Usuario />} />
               <Route path="/loginDoutor" element={<Login />} />
               <Route path="/loginPaciente" element={<LoginPaciente />} />
           </Routes>
       </BrowserRouter>
   );
}

export default AppRoutes;