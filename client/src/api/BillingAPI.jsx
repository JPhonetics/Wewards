import { api, errorMessage } from "./api"


export const billingProducts = async () => {

    try {
        const response = await api.get("billing/products/")
        return response.data

    }catch (error){
        alert(errorMessage(error))
        return null;
    }
}