import FloatingLabel from "react-bootstrap/FloatingLabel"
import Form from "react-bootstrap/Form"


export default function BusinessItemForm({
    item,
    setItem,
}) {

    const handleChange = (event) => {
        const { name, value } = event.target

        setItem((currentItem) => ({
            ...currentItem,
            [name]: value,
        }))
    }

    return (
        <>

            <FloatingLabel
                controlId = "item_name"
                label = "Item Name"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "name"
                    placeholder = "Item Name"
                    value = {item.name}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "item_description"
                label = "Description"
                className = "mb-3"
            >
                <Form.Control
                    as = "textarea"
                    name = "description"
                    placeholder = "Description"
                    value = {item.description}
                    onChange = {handleChange}
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "item_status"
                label = "Status"
                className = "mb-3"
            >
                <Form.Select
                    name = "status"
                    value = {item.status}
                    onChange = {handleChange}
                    required
                >
                    <option value = "draft">
                        Draft
                    </option>

                    <option value = "active">
                        Active
                    </option>

                    <option value = "unavailable">
                        Unavailable
                    </option>

                    <option value = "discontinued">
                        Discontinued
                    </option>
                </Form.Select>
            </FloatingLabel>

        </>
    )
}