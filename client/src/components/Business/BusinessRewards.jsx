import { useEffect, useState } from "react"

import ListGroup from "react-bootstrap/ListGroup"

import {
    getRewards
} from "../../api/BusinessesAPI"


export default function BusinessRewards({
    businessId,
    rewardRefresh,
}) {

    const [rewards, setRewards] = useState([])


    useEffect(() => {

        const loadRewards = async () => {

            const response = await getRewards(
                businessId
            )

            if (response) {
                setRewards(response)
            }
        }

        loadRewards()

    }, [
        businessId,
        rewardRefresh
    ])


    return (

        <ListGroup>

            {rewards.map((reward) => (

                <ListGroup.Item
                    key = {reward.id}
                >

                    <strong>
                        {reward.name}
                    </strong>

                    <div>
                        Reward Type: {reward.reward_type}
                    </div>

                    <div>
                        Amount Required: {reward.amount_required}
                    </div>

                    <div>
                        Status: {reward.status}
                    </div>

                </ListGroup.Item>

            ))}

        </ListGroup>
    )
}