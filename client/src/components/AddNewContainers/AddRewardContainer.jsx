import { useEffect, useState } from "react"

import Card from "react-bootstrap/Card"
import Form from "react-bootstrap/Form"

import Button from "../Buttons"

import {
    BusinessRewardForm
} from "../Forms"

import {
    getBusinessItems,
    getRewardPrograms,
    postReward,
} from "../../api/BusinessesAPI"


export default function AddRewardContainer({
    businessId,
    setShowAddReward,
    setRewardRefresh,
}) {

    const [reward, setReward] = useState({
        name: "",
        reward_program: "",
        reward_type: "",
        description: "",
        qualifying_item: "",
        amount_required: "",
        earned_item: "",
        discount_amount: "",
        discount_percentage: "",
        status: "draft",
        end_date: "",
    })

    const [rewardPrograms, setRewardPrograms] = useState([])
    const [items, setItems] = useState([])


    const rewardComplete =
        reward.name &&
        reward.reward_program &&
        reward.reward_type &&
        reward.amount_required


    useEffect(() => {

        const loadRewardPrograms = async () => {

            const response = await getRewardPrograms(
                businessId
            )

            if (response) {
                setRewardPrograms(response)
            }
        }


        const loadItems = async () => {

            const response = await getBusinessItems(
                businessId
            )

            if (response) {
                setItems(response)
            }
        }


        loadRewardPrograms()
        loadItems()

    }, [businessId])


    const handleSubmit = async (event) => {
        event.preventDefault()

        const rewardData = {
            ...reward,
            qualifying_item:
                reward.qualifying_item || null,
            earned_item:
                reward.earned_item || null,
            discount_amount:
                reward.discount_amount || null,
            discount_percentage:
                reward.discount_percentage || null,
            end_date:
                reward.end_date || null,
        }

        const response = await postReward(
            businessId,
            rewardData
        )

        if (response) {

            setReward({
                name: "",
                reward_program: "",
                reward_type: "",
                description: "",
                qualifying_item: "",
                amount_required: "",
                earned_item: "",
                discount_amount: "",
                discount_percentage: "",
                status: "draft",
                end_date: "",
            })

            setRewardRefresh(
                (currentRefresh) =>
                    currentRefresh + 1
            )

            setShowAddReward(false)
        }
    }


    return (

        <Card className = "mb-4">

            <Card.Body>

                <Card.Title
                    as = "h3"
                    className = "mb-4"
                >
                    Add Reward
                </Card.Title>

                <Form onSubmit = {handleSubmit}>

                    <BusinessRewardForm
                        reward = {reward}
                        setReward = {setReward}
                        rewardPrograms = {rewardPrograms}
                        items = {items}
                    />

                    <div className = "d-flex justify-content-between">

                        <Button
                            type = "button"
                            variant = "secondary"
                            onClick = {
                                () => setShowAddReward(false)
                            }
                        >
                            Cancel
                        </Button>

                        <Button
                            type = "submit"
                            disabled = {!rewardComplete}
                        >
                            Add Reward
                        </Button>

                    </div>

                </Form>

            </Card.Body>

        </Card>
    )
}