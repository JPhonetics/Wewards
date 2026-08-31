import Card from "react-bootstrap/Card"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

import UserProfileForm from "./UserProfileForm"


export default function UserProfileCard({ user, setUser }) {

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
                            Profile
                        </Card.Title>

                        <UserProfileForm
                            user = {user}
                            setUser = {setUser}
                        />

                    </Card.Body>
                </Card>

            </Col>
        </Row>
    )
}