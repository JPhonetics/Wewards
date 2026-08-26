import { api, errorMessage } from "./api"


export const BusinessRegistration = async (registration) => {

    const registrationData = {

        business: {
            name: registration.business.name,
            industry: registration.business.industry,
            website: registration.business.website,
            email: registration.business.email,
            phone_number: registration.business.phone_number,
            logo: registration.business.logo,
        },

        business_location: {
            name: registration.location.name,
            address_line_1: registration.location.address_line_1,
            address_line_2: registration.location.address_line_2,
            city: registration.location.city,
            state_region: registration.location.state_region,
            postal_code: registration.location.postal_code,
            country: registration.location.country,
            timezone: registration.location.timezone,
        },
    }

    try {
        const response = await api.post(
            "businesses/register/",
            registrationData
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const getBusiness = async (businessId) => {

    try {
        const response = await api.get(
            `businesses/${businessId}/`
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const getBusinessStats = async (businessId) => {

    try {
        const response = await api.get(
            `businesses/${businessId}/stats/`
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const updateBusiness = async (
    businessId,
    business
) => {

    try {
        const response = await api.patch(
            `businesses/${businessId}/`,
            business
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const getBusinessStaff = async () => {

    try {
        const response = await api.get(
            "businesses/staff/"
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const getBusinessStaffList = async (businessId) => {

    try {
        const response = await api.get(
            `businesses/${businessId}/staff/`
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const getBusinessLocations = async (businessId) => {

    try {
        const response = await api.get(
            `businesses/${businessId}/locations/`
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const postBusinessLocations = async (
    businessId,
    location,
) => {
    try {
        const response = await api.post(
            `businesses/${businessId}/locations/`,
            location
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}

export const deleteBusinessLocation = async (
    businessId,
    locationId,
) => {
    try {
        await api.delete(
            `businesses/${businessId}/locations/${locationId}/`
        )
        return true

    } catch (error) {
        alert(errorMessage(error))
        return false
    }
}


export const getBusinessItems = async (businessId) => {

    try {
        const response = await api.get(
            `businesses/${businessId}/items/`
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const postBusinessItems = async (
    businessId,
    item,
) => {

    try {
        const response = await api.post(
            `businesses/${businessId}/items/`,
            item
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const deleteBusinessItem = async (
    businessId,
    itemId,
) => {
    try {
        await api.delete(
            `businesses/${businessId}/items/${itemId}/`
        )
        return true

    } catch (error) {
        alert(errorMessage(error))
        return false
    }
}


export const getRewardProgramTypes = async () => {
    try {
        const response = await api.get(
            "rewards/program-types/"
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const getRewardPrograms = async (
    businessId,
) => {

    try {
        const response = await api.get(
            `rewards/${businessId}/reward-programs/`
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const postRewardProgram = async (
    businessId,
    rewardProgram,
) => {
    try {

        const response = await api.post(
            `rewards/${businessId}/reward-programs/`,
            rewardProgram
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const getRewards = async (
    businessId,
) => {
    try {

        const response = await api.get(
            `rewards/${businessId}/rewards/`
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}


export const postReward = async (
    businessId,
    reward,
) => {
    try {

        const response = await api.post(
            `rewards/${businessId}/rewards/`,
            reward
        )
        return response.data

    } catch (error) {
        alert(errorMessage(error))
        return null
    }
}