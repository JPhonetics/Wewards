import { redirect } from "react-router-dom"
import { api, errorMessage } from "./api"


// REGISTER
export const userSignup = async (user) => {

    try {
        const response = await api.post(
            "accounts/signup/",
            user
        )
        
        return response.data

    }catch (error){
        alert(errorMessage(error))
        return null;
    }

}

// Login
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
        const response = await api.get("accounts/user/");
        return response.data;
    } catch {
        return null;
    }
}


//  blocks a route: bounce to login page if there is no token
export const requireLogin = async ()=>{
    const user = await userConfirmation()
    if (!user) throw redirect("/login");
    return null;
}

//  the reverse.... a logged in user has no business on the login page
export const redirectIfLoggedIn = async ()=>{
    const user = await userConfirmation()
    return user ? redirect("/user/dashboard") : null;
}


export const updateUserProfile = async (profile) => {
    try {
        const response = await api.patch(
            "accounts/user/",
            profile
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const updateUserPassword = async (
    currentPassword,
    newPassword
) => {
    try {
        const response = await api.patch(
            "accounts/password/",
            {
                current_password: currentPassword,
                new_password: newPassword,
            }
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}