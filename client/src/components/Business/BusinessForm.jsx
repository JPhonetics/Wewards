import FloatingLabel from "react-bootstrap/FloatingLabel"
import Form from "react-bootstrap/Form"


export default function BusinessForm({
    business,
    setBusiness,
}) {

    const handleChange = (event) => {
        const { name, value } = event.target

        setBusiness((currentBusiness) => ({
            ...currentBusiness,
            [name]: value,
        }))
    }

    return (
        <>

            <FloatingLabel
                controlId = "business_name"
                label = "Business Name"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "name"
                    placeholder = "Business Name"
                    value = {business.name}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "industry"
                label = "Industry"
                className = "mb-3"
            >
                <Form.Select
                    name = "industry"
                    value = {business.industry}
                    onChange = {handleChange}
                    required
                >
                    <option value = "">
                        Select Industry
                    </option>

                    <option value = "Food & Beverage">
                        Food & Beverage
                    </option>

                    <option value = "Retail">
                        Retail
                    </option>

                    <option value = "Service">
                        Service
                    </option>

                    <option value = "Other">
                        Other
                    </option>
                </Form.Select>
            </FloatingLabel>

            <FloatingLabel
                controlId = "business_email"
                label = "Business Email"
                className = "mb-3"
            >
                <Form.Control
                    type = "email"
                    name = "email"
                    placeholder = "Business Email"
                    value = {business.email}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "business_phone_number"
                label = "Business Phone Number"
                className = "mb-3"
            >
                <Form.Control
                    type = "tel"
                    name = "phone_number"
                    placeholder = "Business Phone Number"
                    value = {business.phone_number}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "website"
                label = "Website"
                className = "mb-3"
            >
                <Form.Control
                    type = "url"
                    name = "website"
                    placeholder = "Website"
                    value = {business.website}
                    onChange = {handleChange}
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "logo"
                label = "Logo URL"
                className = "mb-3"
            >
                <Form.Control
                    type = "url"
                    name = "logo"
                    placeholder = "Logo URL"
                    value = {business.logo}
                    onChange = {handleChange}
                />
            </FloatingLabel>

        </>
    )
}