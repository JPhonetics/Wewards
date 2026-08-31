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


export const getBusinessBilling = async (businessId) => {

    const response = await api.get(
        `/billing/business/${businessId}/`
    )

    return response.data
}


export const subscribeBusiness = async (
    businessId,
    priceId,
) => {

    // Send the selected Stripe Price ID to Django
    const response = await api.post(
        `/billing/business/${businessId}/subscribe/`,
        {
            price_id: priceId,
        }
    )

    // Returns checkout_url
    return response.data
}