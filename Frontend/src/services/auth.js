const API_URL = "http://127.0.0.1:2488";
export const registerUser = async (userData) =>{
    const response = await fetch(
        `${API_URL}/auth/register`,
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body: JSON.stringify(userData)
        }
    );

    const data = await response.json();

    return{
        response,
        data
    };
};

export const loginUser = async (loginData) =>{
    const response = await fetch(
        `${API_URL}/auth/login`,
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            credentials: "include",

            body:JSON.stringify(loginData)
        }
    );

    const data = await response.json();

    return{
        response,
        data
    };
};

export const VerifyOtp = async (otpData) => {
    const response = await fetch(`${API_URL}/auth/verify-otp`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(otpData)
        }
    );

    const data = await response.json();
    return  {
        response,
        data
    }
}