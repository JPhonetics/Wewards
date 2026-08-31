import { useEffect, useState } from "react"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import { getCustomerRewards } from "../../../api/RewardsAPI"
import RewardCard from "./RewardCard"


export default function RewardsContainer() {

    const [customerRewards, setCustomerRewards] = useState([])

    useEffect(() => {

        const loadCustomerRewards = async () => {

            const response = await getCustomerRewards()

            if (response) {
                setCustomerRewards(response)
            }
        }

        loadCustomerRewards()

    }, [])

    return (
        <>
            <h2></h2>

            {customerRewards.map((business) => (
                <div
                    key = {business.business_id}
                    className = "mb-5"
                >
                    <h3>{business.business_name}</h3>

                    {business.reward_programs.map((rewardProgram) => (
                        <div
                            key = {rewardProgram.reward_program_id}
                            className = "mb-4"
                        >
                            <h4>
                                {rewardProgram.reward_program_name}
                            </h4>

                            {rewardProgram.program_type === "Points" && (
                                <div className = "mb-3">
                                    Balance: {rewardProgram.balance}
                                </div>
                            )}

                            <Row>
                                {rewardProgram.rewards.map((reward) => (
                                    <Col
                                        key = {reward.id}
                                        xs = {12}
                                        md = {6}
                                        lg = {4}
                                        className = "mb-3"
                                    >
                                        <RewardCard
                                            reward = {reward}
                                        />
                                    </Col>
                                ))}
                            </Row>
                        </div>
                    ))}
                </div>
            ))}
        </>
    )
}