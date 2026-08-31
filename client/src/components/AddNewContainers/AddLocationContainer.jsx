import { useState } from "react"

import Card from "react-bootstrap/Card"
import Form from "react-bootstrap/Form"

import Button from "../Buttons"

import {
    BusinessLocationForm
} from "../Forms"

import {
    postBusinessLocations
} from "../../api/BusinessesAPI"


export default function AddLocationContainer({
    businessId,
    setShowAddLocation,
    setLocationRefresh,
}) {

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

    const locationComplete =
        location.name &&
        location.address_line_1 &&
        location.city &&
        location.state_region &&
        location.postal_code &&
        location.country &&
        location.timezone


    const handleSubmit = async (event) => {
        event.preventDefault()

        const response = await postBusinessLocations(
            businessId,
            location
        )

        if (response) {

            setLocation({
                name: "",
                address_line_1: "",
                address_line_2: "",
                city: "",
                state_region: "",
                postal_code: "",
                country: "",
                timezone: "",
            })

            setLocationRefresh(
                (currentRefresh) =>
                    currentRefresh + 1
            )

            setShowAddLocation(false)
        }
    }


    return (

        <Card className = "mb-4">

            <Card.Body>

                <Card.Title
                    as = "h3"
                    className = "mb-4"
                >
                    Add Location
                </Card.Title>

                <Form onSubmit = {handleSubmit}>

                    <BusinessLocationForm
                        location = {location}
                        setLocation = {setLocation}
                    />

                    <div className = "d-flex justify-content-between">

                        <Button
                            type = "button"
                            variant = "secondary"
                            onClick = {
                                () => setShowAddLocation(false)
                            }
                        >
                            Cancel
                        </Button>

                        <Button
                            type = "submit"
                            disabled = {!locationComplete}
                        >
                            Add Location
                        </Button>

                    </div>

                </Form>

            </Card.Body>

        </Card>
    )
}