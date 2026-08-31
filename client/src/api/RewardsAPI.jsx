import { api, errorMessage } from "./api"


export const getCustomerRewards = async () => {

    try {
        const response = await api.get(
            "rewards/customer/"
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}