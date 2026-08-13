import {useState} from 'react'
import {Link, useNavigate } from 'react-router-dom';

import { registerUser, VerifyOtp } from '../services/auth';

import image from "../images/loging-page.jpg";
import Input from '../components/Input';
import Button from '../components/Button';

const Register = () => {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        name:"",
        email:"",
        password:"",
        role:""
    });

    const [showOtp, setShowOtp] = useState(false);
    const [otp, setOtp] = useState("");
    const [otpError, setOtpError] = useState("");

    const [error, setError] = useState("");

    const handleChange = (e) =>{
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        setError("");

        if(
            !formData.name ||
            !formData.email ||
            !formData.password ||
            !formData.role
        ){
            setError("Please fill all fields.");
            return;
        }try{
            const {response, data} = await registerUser(formData);

            if (response.ok){
                setShowOtp(true)
            }else{
                setError(data.message);
            }
        }catch (error){
            console.error(error);
            setError("Unable to connect to server");
            
        }
    };

    const handleVerifyOtp = async () =>{
        setOtpError("");

        if (!otp){
            setOtpError("Please enter OTP.");
            return;
        }

        try{
            const {response, data} = await VerifyOtp({
                email: formData.email,
                otp: otp
            });

            if (response.ok){
                setShowOtp(false);
                setOtp("");
                setOtpError("");
                navigate("/login", {replace: true})
            }else{
                setOtpError(data.message || "Invalid OTP.")
            }
        }catch (error){
            console.error(error);

            setOtpError("Unable to connect to server.")
        }
    }
    
  return (
    <>
        <div className="min-h-screen flex items-center justify-center bg-[#F8F7F4] p-4">

            <div className="w-full max-w-225 h-137.5 rounded-3xl shadow-lg overflow-hidden bg-[#FFFFFF] flex">

                <div className="w-1/2 p-10">

                    <div className="flex items-center text-3xl font-bold text-[#111827] mb-8">
                        Create new account
                        <span className="ml-1 mt-3 w-2 h-2 rounded-full bg-[#2DD4BF]"></span>
                    </div>
                    <form onSubmit={handleSubmit}>
                        <Input type="text" name="name" value={formData.name}  onChange={handleChange} placeholder="Enter Name"/>
                        <Input type="email" name="email" value={formData.email} onChange={handleChange} placeholder="Enter Email"/>
                        <Input type="password" name="password" value={formData.password} onChange={handleChange} placeholder="Enter Password"/>


                        <div className="mt-1 p-2">
                            <select  name="role" value={formData.role} onChange={handleChange} className="w-46 h-8 rounded-lg border border-[#d9dedd] bg-white px-4 py-1 text-[#333333] outline-none focus:shadow-[0_0_0_3px_rgba(15,129,122,0.15)] ">
                                <option value="">Select your Role</option>
                                <option value="customer">Customer</option>
                                <option value="seller">Seller</option>
                            </select>
                        </div>

                        {error &&(
                            <p className='text-red-500 mt-2'>
                                {error}
                            </p>
                        )}

                    <Button name="Register" type="submit"/>
                    </form>

                    {showOtp && (
                        <div className='fixed inset-0 z-50 flex items-center justify-center bg-black/50'>
                            <div className='w-96 rounded-2xl bg-white p-8 shadow-xl'>
                                <h2 className='text-2xl font-bold'>
                                    Verify your email
                                </h2>
                                <p className='mt-2'>
                                    OTP send to {formData.email}
                                </p>
                                <div className="relative mt-6">

                <input
                    type="text"
                    value={otp}
                    onChange={(e) => setOtp(e.target.value)}
                    placeholder=" "
                    maxLength={6}
                    className="
                        peer
                        w-full
                        rounded-lg
                        border border-[#d9dedd]
                        bg-white
                        px-4 py-3
                        text-[#333333]
                        outline-none
                        transition-all
                        focus:border-[#0f817a]
                        focus:shadow-[0_0_0_3px_rgba(15,129,122,0.15)]
                    "
                />

                <label
                    className="
                        absolute
                        left-4
                        top-1/2
                        -translate-y-1/2
                        bg-white
                        px-1
                        text-[#777777]
                        transition-all

                        peer-focus:top-0
                        peer-focus:text-sm
                        peer-focus:text-[#0f817a]

                        peer-not-placeholder-shown:top-0
                        peer-not-placeholder-shown:text-sm
                    "
                >
                    Enter OTP
                </label>

            </div>

                                {otpError && (
                                    <p className='mt-2 text-red-500'>
                                        {otpError}
                                    </p>
                                )}

                                <Button name="Verify OTP" type="button" onClick={handleVerifyOtp}/>

                            </div>
                        </div>
                    )}

                    <p className='mt-4'>
                        Already have an account?{" "}
                        <Link to="/login" className="text-blue-500 hover:underline">login</Link>
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

export default Register
