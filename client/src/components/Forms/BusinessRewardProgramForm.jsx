import FloatingLabel from "react-bootstrap/FloatingLabel"
import Form from "react-bootstrap/Form"


export default function BusinessRewardProgramForm({
    rewardProgram,
    setRewardProgram,
    rewardProgramTypes,
}) {

    const handleChange = (event) => {
        const { name, value } = event.target

        setRewardProgram((currentRewardProgram) => ({
            ...currentRewardProgram,
            [name]: value,
        }))
    }

    return (
        <>

            <FloatingLabel
                controlId = "reward_program_name"
                label = "Reward Program Name"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "name"
                    placeholder = "Reward Program Name"
                    value = {rewardProgram.name}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_program_description"
                label = "Description"
                className = "mb-3"
            >
                <Form.Control
                    as = "textarea"
                    name = "description"
                    placeholder = "Description"
                    value = {rewardProgram.description}
                    onChange = {handleChange}
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_program_type"
                label = "Reward Program Type"
                className = "mb-3"
            >
                <Form.Select
                    name = "program_type"
                    value = {rewardProgram.program_type}
                    onChange = {handleChange}
                    required
                >
                    <option value = "">
                        Select Reward Program Type
                    </option>

                    {rewardProgramTypes.map((programType) => (

                        <option
                            key = {programType.id}
                            value = {programType.id}
                        >
                            {programType.name}
                        </option>

                    ))}

                </Form.Select>
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_program_start_date"
                label = "Start Date"
                className = "mb-3"
            >
                <Form.Control
                    type = "datetime-local"
                    name = "start_date"
                    value = {rewardProgram.start_date}
                    onChange = {handleChange}
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_program_status"
                label = "Status"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "status"
                    placeholder = "Status"
                    value = {rewardProgram.status}
                    onChange = {handleChange}
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_program_end_date"
                label = "End Date"
                className = "mb-3"
            >
                <Form.Control
                    type = "datetime-local"
                    name = "end_date"
                    value = {rewardProgram.end_date}
                    onChange = {handleChange}
                />
            </FloatingLabel>

        </>
    )
}