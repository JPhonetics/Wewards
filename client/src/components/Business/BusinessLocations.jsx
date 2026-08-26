import { useEffect, useState } from "react"

import Button from "react-bootstrap/Button"
import ListGroup from "react-bootstrap/ListGroup"

import {
    deleteBusinessLocation,
    getBusinessLocations,
} from "../../api/BusinessesAPI"


export default function BusinessLocations({
    businessId,
    locationRefresh,
}) {

    const [locations, setLocations] = useState([])


    useEffect(() => {

        const loadLocations = async () => {

            const response = await getBusinessLocations(
                businessId
            )

            if (response) {
                setLocations(response)
            }
        }

        loadLocations()

    }, [
        businessId,
        locationRefresh
    ])


    const handleDelete = async (locationId) => {

        const response = await deleteBusinessLocation(
            businessId,
            locationId
        )

        if (response) {

            setLocations((currentLocations) =>
                currentLocations.filter(
                    (location) => location.id !== locationId
                )
            )
        }
    }


    return (

        <ListGroup>

            {locations.map((location) => (

                <ListGroup.Item
                    key = {location.id}
                    className = "d-flex justify-content-between align-items-center"
                >

                    <div>

                        <strong>
                            {location.name}
                        </strong>

                        <div>
                            {location.address_line_1}
                        </div>

                        <div>
                            {location.city}, {location.state_region}
                        </div>

                    </div>

                    <Button
                        variant = "danger"
                        onClick = {
                            () => handleDelete(location.id)
                        }
                    >
                        Delete
                    </Button>

                </ListGroup.Item>

            ))}

        </ListGroup>
    )
}