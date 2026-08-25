import axios from 'axios';

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


export const errorMessage = (error)=>{
    const data = error.response?.data;
    if (!data) return "Could not reach the server.";
    return typeof data === "string" ? data : JSON.stringify(data);
}