import { useState } from "react"

import Card from "react-bootstrap/Card"
import Tab from "react-bootstrap/Tab"
import Tabs from "react-bootstrap/Tabs"

import Button from "../Button"

import {
    AddItemContainer,
    AddLocationContainer,
    AddRewardContainer,
    AddRewardProgramContainer,
} from "../AddNewContainers"

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

    const [showAddLocation, setShowAddLocation] = useState(false)
    const [showAddItem, setShowAddItem] = useState(false)
    const [showAddRewardProgram, setShowAddRewardProgram] = useState(false)
    const [showAddReward, setShowAddReward] = useState(false)

    const [locationRefresh, setLocationRefresh] = useState(0)
    const [itemRefresh, setItemRefresh] = useState(0)
    const [rewardProgramRefresh, setRewardProgramRefresh] = useState(0)
    const [rewardRefresh, setRewardRefresh] = useState(0)


    return (

        <Card className = "mb-4">

            <Card.Body>

                <Tabs
                    defaultActiveKey = "overview"
                    className = "mb-4 flex-nowrap"
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

                        {!showAddLocation && (

                            <div className = "d-flex justify-content-end mb-3">

                                <Button
                                    type = "button"
                                    onClick = {
                                        () => setShowAddLocation(true)
                                    }
                                >
                                    Add Location
                                </Button>

                            </div>

                        )}

                        {showAddLocation && (

                            <AddLocationContainer
                                businessId = {businessId}
                                setShowAddLocation = {setShowAddLocation}
                                setLocationRefresh = {setLocationRefresh}
                            />

                        )}

                        <BusinessLocations
                            businessId = {businessId}
                            locationRefresh = {locationRefresh}
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

                        {!showAddItem && (

                            <div className = "d-flex justify-content-end mb-3">

                                <Button
                                    type = "button"
                                    onClick = {
                                        () => setShowAddItem(true)
                                    }
                                >
                                    Add Item
                                </Button>

                            </div>

                        )}

                        {showAddItem && (

                            <AddItemContainer
                                businessId = {businessId}
                                setShowAddItem = {setShowAddItem}
                                setItemRefresh = {setItemRefresh}
                            />

                        )}

                        <BusinessItems
                            businessId = {businessId}
                            itemRefresh = {itemRefresh}
                        />

                    </Tab>

                    <Tab
                        eventKey = "programs"
                        title = "Reward Programs"
                    >

                        {!showAddRewardProgram && (

                            <div className = "d-flex justify-content-end mb-3">

                                <Button
                                    type = "button"
                                    onClick = {
                                        () => setShowAddRewardProgram(true)
                                    }
                                >
                                    Add Reward Program
                                </Button>

                            </div>

                        )}

                        {showAddRewardProgram && (

                            <AddRewardProgramContainer
                                businessId = {businessId}
                                setShowAddRewardProgram = {setShowAddRewardProgram}
                                setRewardProgramRefresh = {setRewardProgramRefresh}
                            />

                        )}

                        <BusinessRewardPrograms
                            businessId = {businessId}
                            rewardProgramRefresh = {rewardProgramRefresh}
                        />

                    </Tab>

                    <Tab
                        eventKey = "rewards"
                        title = "Rewards"
                    >

                        {!showAddReward && (

                            <div className = "d-flex justify-content-end mb-3">

                                <Button
                                    type = "button"
                                    onClick = {
                                        () => setShowAddReward(true)
                                    }
                                >
                                    Add Reward
                                </Button>

                            </div>

                        )}

                        {showAddReward && (

                            <AddRewardContainer
                                businessId = {businessId}
                                setShowAddReward = {setShowAddReward}
                                setRewardRefresh = {setRewardRefresh}
                            />

                        )}

                        <BusinessRewards
                            businessId = {businessId}
                            rewardRefresh = {rewardRefresh}
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