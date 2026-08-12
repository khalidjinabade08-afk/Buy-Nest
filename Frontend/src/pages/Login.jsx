import React, { useState } from 'react'
import { Link,useNavigate } from 'react-router-dom'
import { loginUser } from '../services/auth'
import image from "../images/loging-page.jpg"
import Input from '../components/Input'
import Button from '../components/Button'

const Loging = () => {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        email:"",
        password:""
    });
     
    const [error, setError] = useState("");

    const handleChange =(e)=>{
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
            });
        };

    const handleSubmit = async (e) =>{
        e.preventDefault();
        if(!formData.email || !formData.password){
            setError("Please enter email and password")
            return;

        }try{
            const {response, data} = await loginUser(formData);
            if (response.ok){
                navigate("/dashboard")
            }else{
                setError(data.message);
            }
        } catch (error){
            console.error(error)
            setError("Unable to connect to server.")
        }
    };
    
  return (
    <>
      <div className="min-h-screen flex items-center justify-center bg-[#F8F7F4] p-4">

            <div className="w-full max-w-225 h-137.5 rounded-3xl shadow-lg overflow-hidden bg-[#FFFFFF] flex">

                <div className="w-1/2 p-10">

                    <div className="flex items-center text-3xl font-bold text-[#111827] mb-8">
                        Sing in to your account
                        <span className="ml-1 mt-3 w-2 h-2 rounded-full bg-[#2DD4BF]"></span>
                    </div>
                    <form onSubmit={handleSubmit}>
                        <Input type="email" name="email" value={formData.email} onChange={handleChange} placeholder="Enter Email"/>
                        <Input type="password" name="password" value={formData.password} onChange={handleChange} placeholder="Enter Password"/>

                        <Button name="Sign in" type="submit"/>
                    </form>

                    <p className='mt-4'>
                        Don't Have an account?{" "}
                        <Link to="/register">Register</Link>
                    </p>

                </div>

                <div className="relative w-1/2 h-full overflow-hidden">
                    <img
                        src={image}
                        alt="Create account"
                        className="w-full max-h-150 object-cover"
                    />
                </div>

            </div>
      </div>

    </>
  )
}

export default Loging
