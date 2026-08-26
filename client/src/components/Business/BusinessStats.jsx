import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

import BusinessStatsCard from "./BusinessStatsCard"


export default function BusinessStats({ stats }) {

    return (

        <div className = "mb-4">

            {/* <h2 className = "mb-3">
                Stats
            </h2> */}

            <Row>

                <Col
                    xs = {6}
                    md = {4}
                    lg = {2}
                    className = "mb-3"
                >
                    <BusinessStatsCard
                        count = {stats.locations}
                        label = "Locations"
                    />
                </Col>

                <Col
                    xs = {6}
                    md = {4}
                    lg = {2}
                    className = "mb-3"
                >
                    <BusinessStatsCard
                        count = {stats.staff}
                        label = "Staff"
                    />
                </Col>

                <Col
                    xs = {6}
                    md = {4}
                    lg = {2}
                    className = "mb-3"
                >
                    <BusinessStatsCard
                        count = {stats.items}
                        label = "Items"
                    />
                </Col>

                <Col
                    xs = {6}
                    md = {4}
                    lg = {2}
                    className = "mb-3"
                >
                    <BusinessStatsCard
                        count = {stats.rewards ?? 0}
                        label = "Rewards"
                    />
                </Col>

                <Col
                    xs = {6}
                    md = {4}
                    lg = {2}
                    className = "mb-3"
                >
                    <BusinessStatsCard
                        count = {stats.active_customers ?? 0}
                        label = "Active Customers"
                    />
                </Col>

                <Col
                    xs = {6}
                    md = {4}
                    lg = {2}
                    className = "mb-3"
                >
                    <BusinessStatsCard
                        count = {stats.ready_to_redeem ?? 0}
                        label = "Ready to Redeem"
                    />
                </Col>

            </Row>

        </div>
    )
}