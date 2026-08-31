import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

import BusinessDashboardCard from "./BusinessDashboardCard"


export default function BusinessDashboardContainer({
    businessStaff,
}) {

    const singleBusiness = businessStaff.length === 1

    return (

        <Row
            className = {
                singleBusiness
                    ? "justify-content-center"
                    : ""
            }
        >

            {businessStaff.map((staff) => (

                <Col
                    key = {staff.id}
                    xs = {12}
                    md = {6}
                    lg = {4}
                    className = "mb-4"
                >
                    <BusinessDashboardCard
                        staff = {staff}
                    />
                </Col>

            ))}

        </Row>
    )
}