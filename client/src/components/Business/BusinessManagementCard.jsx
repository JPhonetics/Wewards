import Card from "react-bootstrap/Card"
import Tab from "react-bootstrap/Tab"
import Tabs from "react-bootstrap/Tabs"

import BusinessOverview from "./BusinessOverview"
import BusinessInfo from "./BusinessInfo"
import BusinessLocations from "./BusinessLocations"
import BusinessStaff from "./BusinessStaff"
import BusinessItems from "./BusinessItems"
import BusinessRewardPrograms from "./BusinessRewardPrograms"
import BusinessRewards from "./BusinessRewards"
import BusinessCustomerRewards from "./BusinessCustomerRewards"
import BusinessBilling from "./BusinessBilling"


export default function BusinessManagementCard({
    business,
    businessId,
    businessStaff,
    setBusinessStaff,
}) {

    return (

        <Card className = "mb-4">

            <Card.Body>

                <Tabs
                    defaultActiveKey = "overview"
                    className = "mb-4"
                >

                    <Tab
                        eventKey = "overview"
                        title = "Overview"
                    >
                        <BusinessOverview
                            businessId = {businessId}
                        />
                    </Tab>

                    <Tab
                        eventKey = "info"
                        title = "Business Info"
                    >
                        <BusinessInfo
                            business = {business}
                            businessStaff = {businessStaff}
                            setBusinessStaff = {setBusinessStaff}
                        />
                    </Tab>

                    <Tab
                        eventKey = "locations"
                        title = "Locations"
                    >
                        <BusinessLocations
                            businessId = {businessId}
                        />
                    </Tab>

                    <Tab
                        eventKey = "staff"
                        title = "Staff"
                    >
                        <BusinessStaff
                            businessId = {businessId}
                        />
                    </Tab>

                    <Tab
                        eventKey = "items"
                        title = "Items"
                    >
                        <BusinessItems
                            businessId = {businessId}
                        />
                    </Tab>

                    <Tab
                        eventKey = "programs"
                        title = "Reward Programs"
                    >
                        <BusinessRewardPrograms
                            businessId = {businessId}
                        />
                    </Tab>

                    <Tab
                        eventKey = "rewards"
                        title = "Rewards"
                    >
                        <BusinessRewards
                            businessId = {businessId}
                        />
                    </Tab>

                    <Tab
                        eventKey = "customers"
                        title = "Customer Rewards"
                    >
                        <BusinessCustomerRewards
                            businessId = {businessId}
                        />
                    </Tab>

                    <Tab
                        eventKey = "billing"
                        title = "Billing"
                    >
                        <BusinessBilling
                            businessId = {businessId}
                        />
                    </Tab>

                </Tabs>

            </Card.Body>

        </Card>
    )
}