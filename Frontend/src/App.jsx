import "./App.css";
import {Routes, Route} from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/Login";
import OTP_page from "./pages/OTP_page";

function App() {
  return (
    <>
    {/* <OTP_page/> */}
      <Routes>
        {/* <Route path="/" element={<OTP_page />}/> */}
        <Route path="/" element={<Login />}/>
        <Route path="/login" element={<Login />}/>
        <Route path="/register" element={<Register />}/>
        {/* <Route path="/dashboard" element={<Dashboard />}/> */}
      </Routes>
      
    </>
  );
}

export default App;