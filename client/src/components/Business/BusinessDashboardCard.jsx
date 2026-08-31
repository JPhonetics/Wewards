import { Link } from "react-router-dom"
import Card from "react-bootstrap/Card"


export default function BusinessDashboardCard({ staff }) {

    const business = staff.business

    return (

        <Card
            as = {Link}
            to = {`/business/${business.id}`}
            className = "mb-3 text-decoration-none"
        >

            <div
                className = "d-flex align-items-center justify-content-center pt-4"
                style = {{
                    height: "140px",
                }}
            >

                {business.logo ? (
                    <img
                        src = {business.logo}
                        alt = {`${business.name} logo`}
                        className = "img-fluid"
                        style = {{
                            maxHeight: "100px",
                            maxWidth: "160px",
                        }}
                    />
                ) : (
                    <strong>
                        Wewards
                    </strong>
                )}

            </div>

            <Card.Body>

                <Card.Title className = "mb-1">
                    {business.name}
                </Card.Title>

                <Card.Text className = "mb-1">
                    {business.industry}
                </Card.Text>

                <Card.Text className = "mb-0">
                    Role: {staff.role_display}
                </Card.Text>

            </Card.Body>

        </Card>
    )
}