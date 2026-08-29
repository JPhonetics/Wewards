import { useEffect, useState } from "react"

import Card from "react-bootstrap/Card"
import Form from "react-bootstrap/Form"

import Button from "../Buttons"

import {
    BusinessRewardProgramForm
} from "../Forms"

import {
    getRewardProgramTypes,
    postRewardProgram,
} from "../../api/BusinessesAPI"


export default function AddRewardProgramContainer({
    businessId,
    setShowAddRewardProgram,
    setRewardProgramRefresh,
}) {

    const [rewardProgram, setRewardProgram] = useState({
        name: "",
        description: "",
        program_type: "",
        start_date: "",
        status: "draft",
        end_date: "",
    })

    const [rewardProgramTypes, setRewardProgramTypes] = useState([])


    const rewardProgramComplete =
        rewardProgram.name &&
        rewardProgram.program_type


    useEffect(() => {

        const loadRewardProgramTypes = async () => {

            const response = await getRewardProgramTypes()

            if (response) {
                setRewardProgramTypes(response)
            }
        }

        loadRewardProgramTypes()

    }, [])


    const handleSubmit = async (event) => {
        event.preventDefault()

        const rewardProgramData = {
            ...rewardProgram,
            start_date:
                rewardProgram.start_date || null,
            end_date:
                rewardProgram.end_date || null,
        }

        const response = await postRewardProgram(
            businessId,
            rewardProgramData
        )

        if (response) {

            setRewardProgram({
                name: "",
                description: "",
                program_type: "",
                start_date: "",
                status: "draft",
                end_date: "",
            })

            setRewardProgramRefresh(
                (currentRefresh) =>
                    currentRefresh + 1
            )

            setShowAddRewardProgram(false)
        }
    }


    return (

        <Card className = "mb-4">

            <Card.Body>

                <Card.Title
                    as = "h3"
                    className = "mb-4"
                >
                    Add Reward Program
                </Card.Title>

                <Form onSubmit = {handleSubmit}>

                    <BusinessRewardProgramForm
                        rewardProgram = {rewardProgram}
                        setRewardProgram = {setRewardProgram}
                        rewardProgramTypes = {rewardProgramTypes}
                    />

                    <div className = "d-flex justify-content-between">

                        <Button
                            type = "button"
                            variant = "secondary"
                            onClick = {
                                () => setShowAddRewardProgram(false)
                            }
                        >
                            Cancel
                        </Button>

                        <Button
                            type = "submit"
                            disabled = {!rewardProgramComplete}
                        >
                            Add Reward Program
                        </Button>

                    </div>

                </Form>

            </Card.Body>

        </Card>
    )
}