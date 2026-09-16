import { useEffect,useState} from 'react'
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

    const [isResending, setIsResending] = useState(false);
    const [resendSeconds, setResendSeconds] = useState(0);
    const [otpMessage, setOtpMessage] = useState("");

    useEffect(() => {
        if (resendSeconds <= 0) return;

        const timer = setInterval(() => {
            setResendSeconds((prevSeconds) => prevSeconds - 1);
        }, 1000);

        return () => clearInterval(timer);
    }, [resendSeconds]);

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

    const handleVerifyOtp = async () => {
        setOtpError("");

        if (!otp) {
            setOtpError("Please enter OTP.");
            return;
        }

        if (otp.length !== 6) {
            setOtpError("OTP must contain 6 digits.");
            return;
        }

        try {
            const { response, data } = await VerifyOtp({
                email: formData.email,
                otp: otp
            });

            if (response.ok) {
                setShowOtp(false);
                setOtp("");
                setOtpError("");
                setOtpMessage("");
                setResendSeconds(0);

                navigate("/login", { replace: true });
            } else {
                setOtpError(data.message || "Invalid OTP.");
            }
        } catch (error) {
            console.error(error);
            setOtpError("Unable to connect to server.");
        }
    };

    const handleCancelOtp = () => {
        setShowOtp(false);
        setOtp("");
        setOtpError("");
        setOtpMessage("");
        setResendSeconds(0);
    };

    const handleResendOtp = async () => {
        if (resendSeconds > 0 || isResending) {
            return;
        }

        setOtpError("");
        setOtpMessage("");
        setIsResending(true);

        try {
            // Registration API generates and sends a new OTP
            const { response, data } = await registerUser(formData);

            if (response.ok) {
                setOtp("");
                setOtpMessage("A new OTP has been sent to your email.");
                setResendSeconds(30);
            } else {
                setOtpError(data.message || "Unable to resend OTP.");
            }
        } catch (error) {
            console.error(error);
            setOtpError("Unable to connect to server.");
        } finally {
            setIsResending(false);
        }
    };
    
  return (
    <>
        <div className="min-h-screen flex items-center justify-center bg-[#F8F7F4] p-4">
            <div className="w-full max-w-225 h-137.5 rounded-3xl shadow-lg overflow-hidden bg-white flex">

                {/* Left side */}
                <div className="w-1/2 p-10">
                    <div className="flex items-center text-3xl font-bold text-[#111827] mb-8">
                        Create new account

                        <span className="ml-1 mt-3 w-2 h-2 rounded-full bg-[#2DD4BF]"></span>
                    </div>

                    {/* Registration form */}
                    <form onSubmit={handleSubmit}>
                        <Input
                            type="text"
                            name="name"
                            value={formData.name}
                            onChange={handleChange}
                            placeholder="Enter Name"
                        />

                        <Input
                            type="email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            placeholder="Enter Email"
                        />

                        <Input
                            type="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            placeholder="Enter Password"
                        />

                        <div className="mt-1 p-2">
                            <select
                                name="role"
                                value={formData.role}
                                onChange={handleChange}
                                className="
                                    w-46 h-8 rounded-lg
                                    border border-[#d9dedd]
                                    bg-white px-4 py-1
                                    text-[#333333]
                                    outline-none
                                    focus:border-[#0f817a]
                                    focus:shadow-[0_0_0_3px_rgba(15,129,122,0.15)]
                                "
                            >
                                <option value="">Select your Role</option>
                                <option value="customer">Customer</option>
                                <option value="seller">Seller</option>
                            </select>
                        </div>

                        {error && (
                            <p className="mt-2 text-red-500">
                                {error}
                            </p>
                        )}

                        <Button
                            name="Register"
                            type="submit"
                        />
                    </form>

                    <p className="mt-4">
                        Already have an account?{" "}

                        <Link
                            to="/login"
                            className="text-blue-500 hover:underline"
                        >
                            Login
                        </Link>
                    </p>
                </div>

                {/* Right-side image */}
                <div className="relative w-1/2 h-full overflow-hidden">
                    <img
                        src={image}
                        alt="Create account"
                        className="w-full h-full object-cover"
                    />
                </div>
            </div>
        </div>

        {/* OTP popup */}
        {showOtp && (
            <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">
                <div className="w-full max-w-96 rounded-2xl bg-white p-8 shadow-xl">

                    {/* Popup heading and close button */}
                    <div className="flex items-start justify-between">
                        <div>
                            <h2 className="text-2xl font-bold text-[#111827]">
                                Verify your email
                            </h2>

                            <p className="mt-2 text-sm text-gray-600">
                                OTP sent to {formData.email}
                            </p>
                        </div>

                        <button
                            type="button"
                            onClick={handleCancelOtp}
                            className="text-2xl leading-none text-gray-400 hover:text-red-500"
                            aria-label="Cancel OTP verification"
                        >
                            &times;
                        </button>
                    </div>

                    {/* OTP input */}
                    <div className="relative mt-6">
                        <input
                            type="text"
                            inputMode="numeric"
                            value={otp}
                            onChange={(e) => {
                                const value = e.target.value
                                    .replace(/\D/g, "")
                                    .slice(0, 6);

                                setOtp(value);
                                setOtpError("");
                            }}
                            onKeyDown={(e) => {
                                if (e.key === "Enter") {
                                    handleVerifyOtp();
                                }
                            }}
                            placeholder=" "
                            maxLength={6}
                            autoFocus
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
                                pointer-events-none
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

                    {/* OTP error */}
                    {otpError && (
                        <p className="mt-2 text-sm text-red-500">
                            {otpError}
                        </p>
                    )}

                    {/* OTP success message */}
                    {otpMessage && !otpError && (
                        <p className="mt-2 text-sm text-green-600">
                            {otpMessage}
                        </p>
                    )}

                    {/* Verify button */}
                    <Button
                        name="Verify OTP"
                        type="button"
                        onClick={handleVerifyOtp}
                    />

                    {/* Cancel and resend buttons */}
                    <div className="mt-4 flex items-center justify-between">

                        <button
                            type="button"
                            onClick={handleResendOtp}
                            disabled={resendSeconds > 0 || isResending}
                            className="
                                text-sm font-medium
                                text-[#0f817a]
                                hover:underline
                                disabled:cursor-not-allowed
                                disabled:text-gray-400
                                disabled:no-underline
                            "
                        >
                            {isResending
                                ? "Sending..."
                                : resendSeconds > 0
                                ? `Resend OTP in ${resendSeconds}s`
                                : "Resend OTP"}
                        </button>
                    </div>
                </div>
            </div>
        )}
    </>
);
};

export default Register;