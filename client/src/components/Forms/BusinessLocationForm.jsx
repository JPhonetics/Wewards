import FloatingLabel from "react-bootstrap/FloatingLabel"
import Form from "react-bootstrap/Form"


export default function BusinessLocationForm({
    location,
    setLocation,
}) {

    const handleChange = (event) => {
        const { name, value } = event.target

        setLocation((currentLocation) => ({
            ...currentLocation,
            [name]: value,
        }))
    }

    return (
        <>

            <FloatingLabel
                controlId = "location_name"
                label = "Location Name"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "name"
                    placeholder = "Location Name"
                    value = {location.name}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "address_line_1"
                label = "Address"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "address_line_1"
                    placeholder = "Address"
                    value = {location.address_line_1}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "address_line_2"
                label = "Address Line 2"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "address_line_2"
                    placeholder = "Address Line 2"
                    value = {location.address_line_2}
                    onChange = {handleChange}
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "city"
                label = "City"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "city"
                    placeholder = "City"
                    value = {location.city}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "state_region"
                label = "State / Region"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "state_region"
                    placeholder = "State / Region"
                    value = {location.state_region}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "postal_code"
                label = "Postal Code"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "postal_code"
                    placeholder = "Postal Code"
                    value = {location.postal_code}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "location_country"
                label = "Country"
                className = "mb-3"
            >
                <Form.Select
                    name = "country"
                    value = {location.country}
                    onChange = {handleChange}
                    required
                >
                    <option value = "">
                        Select Country
                    </option>

                    <option value = "US">
                        United States
                    </option>

                    <option value = "CA">
                        Canada
                    </option>
                </Form.Select>
            </FloatingLabel>

            <FloatingLabel
                controlId = "timezone"
                label = "Timezone"
                className = "mb-3"
            >
                <Form.Select
                    name = "timezone"
                    value = {location.timezone}
                    onChange = {handleChange}
                    required
                >
                    <option value = "">
                        Select Timezone
                    </option>

                    <option value = "America/New_York">
                        Eastern Time
                    </option>

                    <option value = "America/Chicago">
                        Central Time
                    </option>

                    <option value = "America/Denver">
                        Mountain Time
                    </option>

                    <option value = "America/Phoenix">
                        Arizona Time
                    </option>

                    <option value = "America/Los_Angeles">
                        Pacific Time
                    </option>

                    <option value = "America/Anchorage">
                        Alaska Time
                    </option>

                    <option value = "Pacific/Honolulu">
                        Hawaii Time
                    </option>
                </Form.Select>
            </FloatingLabel>

        </>
    )
}