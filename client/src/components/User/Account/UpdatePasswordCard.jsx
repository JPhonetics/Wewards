import Card from "react-bootstrap/Card"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

import UpdatePasswordForm from "./UpdatePasswordForm"


export default function UpdatePasswordCard() {

    return (

        <Row className = "justify-content-center">
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
                            Update Password
                        </Card.Title>

                        <UpdatePasswordForm />

                    </Card.Body>
                </Card>

            </Col>
        </Row>
    )
}