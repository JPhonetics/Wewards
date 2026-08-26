import Card from "react-bootstrap/Card"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

import BusinessLocationForm from "./BusinessLocationForm"


export default function BusinessLocationCard({
    location,
    setLocation,
}) {

    return (

        <Row className = "justify-content-center mb-4">
            <Col
                xs = {12}
                md = {10}
                lg = {8}
            >

                <Card>
                    <Card.Body>

                        <Card.Title
                            as = "h2"
                            className = "text-center mb-4"
                        >
                            Business Location
                        </Card.Title>

                        <BusinessLocationForm
                            location = {location}
                            setLocation = {setLocation}
                        />

                    </Card.Body>
                </Card>

            </Col>
        </Row>
    )
}