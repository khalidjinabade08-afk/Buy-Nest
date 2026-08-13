import "./App.css";
import {Routes, Route, Navigate ,BrowserRouter} from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/Login";
import Customer from "./pages/Customer";
import Seller from "./pages/Seller";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/Login" replace/>}/>
        <Route path="/login" element={<Login />}/>
        <Route path="/register" element={<Register />}/>
        <Route path="/seller" element={<Seller />}/>
        <Route path="/customer" element={<Customer/>}/>
      </Routes>
      
    </BrowserRouter>
  );
}

export default App;