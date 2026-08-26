import FloatingLabel from "react-bootstrap/FloatingLabel"
import Form from "react-bootstrap/Form"


export default function BusinessRewardForm({
    reward,
    setReward,
    rewardPrograms,
    items,
}) {

    const handleChange = (event) => {
        const { name, value } = event.target

        setReward((currentReward) => ({
            ...currentReward,
            [name]: value,
        }))
    }


    return (
        <>

            <FloatingLabel
                controlId = "reward_name"
                label = "Reward Name"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "name"
                    placeholder = "Reward Name"
                    value = {reward.name}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_program"
                label = "Reward Program"
                className = "mb-3"
            >
                <Form.Select
                    name = "reward_program"
                    value = {reward.reward_program}
                    onChange = {handleChange}
                    required
                >
                    <option value = "">
                        Select Reward Program
                    </option>

                    {rewardPrograms.map((rewardProgram) => (

                        <option
                            key = {rewardProgram.id}
                            value = {rewardProgram.id}
                        >
                            {rewardProgram.name}
                        </option>

                    ))}

                </Form.Select>
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_type"
                label = "Reward Type"
                className = "mb-3"
            >
                <Form.Select
                    name = "reward_type"
                    value = {reward.reward_type}
                    onChange = {handleChange}
                    required
                >
                    <option value = "">
                        Select Reward Type
                    </option>

                    <option value = "discount_amount">
                        Discount Amount
                    </option>

                    <option value = "discount_percentage">
                        Discount Percentage
                    </option>

                    <option value = "free_item">
                        Free Item
                    </option>
                </Form.Select>
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_description"
                label = "Description"
                className = "mb-3"
            >
                <Form.Control
                    as = "textarea"
                    name = "description"
                    placeholder = "Description"
                    value = {reward.description}
                    onChange = {handleChange}
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "qualifying_item"
                label = "Qualifying Item"
                className = "mb-3"
            >
                <Form.Select
                    name = "qualifying_item"
                    value = {reward.qualifying_item}
                    onChange = {handleChange}
                >
                    <option value = "">
                        None
                    </option>

                    {items.map((item) => (

                        <option
                            key = {item.id}
                            value = {item.id}
                        >
                            {item.name}
                        </option>

                    ))}

                </Form.Select>
            </FloatingLabel>

            <FloatingLabel
                controlId = "amount_required"
                label = "Amount Required"
                className = "mb-3"
            >
                <Form.Control
                    type = "number"
                    name = "amount_required"
                    placeholder = "Amount Required"
                    value = {reward.amount_required}
                    onChange = {handleChange}
                    min = "1"
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "earned_item"
                label = "Earned Item"
                className = "mb-3"
            >
                <Form.Select
                    name = "earned_item"
                    value = {reward.earned_item}
                    onChange = {handleChange}
                >
                    <option value = "">
                        None
                    </option>

                    {items.map((item) => (

                        <option
                            key = {item.id}
                            value = {item.id}
                        >
                            {item.name}
                        </option>

                    ))}

                </Form.Select>
            </FloatingLabel>

            <FloatingLabel
                controlId = "discount_amount"
                label = "Discount Amount"
                className = "mb-3"
            >
                <Form.Control
                    type = "number"
                    name = "discount_amount"
                    placeholder = "Discount Amount"
                    value = {reward.discount_amount}
                    onChange = {handleChange}
                    min = "0"
                    step = "0.01"
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "discount_percentage"
                label = "Discount Percentage"
                className = "mb-3"
            >
                <Form.Control
                    type = "number"
                    name = "discount_percentage"
                    placeholder = "Discount Percentage"
                    value = {reward.discount_percentage}
                    onChange = {handleChange}
                    min = "0"
                    max = "100"
                    step = "0.01"
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_status"
                label = "Status"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "status"
                    placeholder = "Status"
                    value = {reward.status}
                    onChange = {handleChange}
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "reward_end_date"
                label = "End Date"
                className = "mb-3"
            >
                <Form.Control
                    type = "datetime-local"
                    name = "end_date"
                    value = {reward.end_date}
                    onChange = {handleChange}
                />
            </FloatingLabel>

        </>
    )
}