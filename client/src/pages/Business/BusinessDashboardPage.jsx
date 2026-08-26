import { useOutletContext } from "react-router-dom"
import Container from "react-bootstrap/Container"

import {
    BusinessDashboardContainer
} from "../../components/Business"


export default function BusinessDashboardPage() {

    const {
        businessStaff,
    } = useOutletContext()

    return (

        <Container className = "py-4">

            <h1 className = "mb-4">
                Businesses
            </h1>

            <BusinessDashboardContainer
                businessStaff = {businessStaff}
            />

        </Container>
    )
}