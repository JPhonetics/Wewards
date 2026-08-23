import { redirect } from "react-router-dom";
import axios from "axios";

export const api = axios.create({
    baseURL: "/api/v1/",
    withCredentials:true
})

const refreshAccessToken=()=>{
    return axios.post("/api/v1/accounts/refresh/",{},{withCredentials:true})
}

api.interceptors.response.use(
    // On success do nothing
    (response)=>response,
    // on failed/error (401) what to do
    async (error)=>{
        const originalRequest = error.config;

        const isRefreshCall = originalRequest?.url?.includes("accounts/refresh")

        if (error.response?.status === 401 && !originalRequest._retry && !isRefreshCall){
            originalRequest._retry = true
            try {
                await refreshAccessToken();
                return api(originalRequest)
            }catch(refreshError){
                return Promise.reject(refreshError)
            }
        }
        return Promise.reject(error)
    }
)


const errorMessage = (error)=>{
    const data = error.response?.data;
    if (!data) return "Could not reach the server.";
    return typeof data === "string" ? data : JSON.stringify(data);
}


// REGISTER and Login
export const userLogin = async (username, password) => {
    const credentials = username.includes("@")
        ? { email: username, password }
        : { phone_number: username, password }

    try {
        const response = await api.post(
            "accounts/login/",
            credentials
        )
        
        return response.data

    }catch (error){
        alert(errorMessage(error))
        return null;
    }

}

export const userLogOut = async () =>{
    try{
        await api.post("accounts/logout/")
    }catch(error){
        console.error("Logout request failed;", error)
    }
    return null

}
export const userConfirmation = async () => {

    try{
        const response = await api.get("accounts/");
        return response.data;
    } catch (error){
        return null;
    }
}


//  blocks a route: bounce to login page if there is no token
export const requireLogin = async ()=>{
    const user = await userConfirmation()
    if (!user) throw redirect("/");
    return null;
}

//  the reverse.... a logged in user has no business on the login page
export const redirectIfLoggedIn = async ()=>{
    const user = await userConfirmation()
    return user ? redirect("/home") : null;
}