import { useEffect, useState } from "react"

import ListGroup from "react-bootstrap/ListGroup"

import {
    getRewardPrograms
} from "../../api/BusinessesAPI"


export default function BusinessRewardPrograms({
    businessId,
    rewardProgramRefresh,
}) {

    const [rewardPrograms, setRewardPrograms] = useState([])


    useEffect(() => {

        const loadRewardPrograms = async () => {

            const response = await getRewardPrograms(
                businessId
            )

            if (response) {
                setRewardPrograms(response)
            }
        }

        loadRewardPrograms()

    }, [
        businessId,
        rewardProgramRefresh
    ])


    return (

        <ListGroup>

            {rewardPrograms.map((rewardProgram) => (

                <ListGroup.Item
                    key = {rewardProgram.id}
                >

                    <strong>
                        {rewardProgram.name}
                    </strong>

                    <div>
                        Program Type: {rewardProgram.program_type_name}
                    </div>

                    <div>
                        Status: {rewardProgram.status}
                    </div>

                </ListGroup.Item>

            ))}

        </ListGroup>
    )
}