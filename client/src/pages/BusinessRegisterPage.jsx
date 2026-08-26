import { useState } from "react"
import {
    useNavigate,
    useOutletContext
} from "react-router-dom"

import Button from "react-bootstrap/Button"
import Container from "react-bootstrap/Container"

import {
    BusinessCard,
    BusinessLocationCard
} from "../components/Business"

import {
    BusinessRegistration,
    getBusinessStaff
} from "../api/BusinessesAPI"


export default function RegisterBusinessPage() {

    const {
        setBusinessStaff,
    } = useOutletContext()

    const [business, setBusiness] = useState({
        name: "",
        industry: "",
        email: "",
        phone_number: "",
        website: "",
        logo: "",
    })

    const [location, setLocation] = useState({
        name: "",
        address_line_1: "",
        address_line_2: "",
        city: "",
        state_region: "",
        postal_code: "",
        country: "",
        timezone: "",
    })

    const navigate = useNavigate()

    const businessComplete =
        business.name &&
        business.industry &&
        business.email &&
        business.phone_number

    const locationComplete =
        location.name &&
        location.address_line_1 &&
        location.city &&
        location.state_region &&
        location.postal_code &&
        location.country &&
        location.timezone

    const handleRegistration = async (event) => {
        event.preventDefault()

        const registration = {
            business,
            location,
        }

        const registeredBusiness = await BusinessRegistration(
            registration
        )

        if (!registeredBusiness) return

        const staff = await getBusinessStaff()

        if (staff) {
            setBusinessStaff(staff)
        }

        navigate("/business/dashboard")
    }

    return (

        <Container className = "py-4">

            <form onSubmit = {handleRegistration}>

                <BusinessCard
                    business = {business}
                    setBusiness = {setBusiness}
                />

                <BusinessLocationCard
                    location = {location}
                    setLocation = {setLocation}
                />

                <div className = "text-center">

                    <Button
                        type = "submit"
                        variant = "primary"
                        disabled = {
                            !businessComplete ||
                            !locationComplete
                        }
                    >
                        Register Business
                    </Button>

                </div>

            </form>

        </Container>
    )
}