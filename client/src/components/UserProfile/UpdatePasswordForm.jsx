import { useState } from "react"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import FloatingLabel from "react-bootstrap/FloatingLabel"

import { updateUserPassword } from "../../api/AccountsAPI"


export default function UpdatePasswordForm() {

    const [passwords, setPasswords] = useState({
        current_password: "",
        new_password: "",
        confirm_password: "",
    })

    // Update password useState fields
    const handleChange = (event) => {
        const { name, value } = event.target

        setPasswords((currentPasswords) => ({
            ...currentPasswords,
            [name]: value,
        }))
    }

    // New password and confirmation must match
    const passwordsMatch =
        passwords.new_password === passwords.confirm_password

    // Require all fields before allowing submit
    const formComplete =
        passwords.current_password &&
        passwords.new_password &&
        passwords.confirm_password

    // Send the password change
    const handleSubmit = async (event) => {
        event.preventDefault()

        if (!passwordsMatch) {
            return
        }

        const response = await updateUserPassword(
            passwords.current_password,
            passwords.new_password
        )

        if (response) {
            setPasswords({
                current_password: "",
                new_password: "",
                confirm_password: "",
            })
        }
    }

    return (
        <Form onSubmit = {handleSubmit}>

            <FloatingLabel
                controlId = "current_password"
                label = "Current Password"
                className = "mb-3"
            >
                <Form.Control
                    type = "password"
                    name = "current_password"
                    placeholder = "Current Password"
                    value = {passwords.current_password}
                    onChange = {handleChange}
                />
            </FloatingLabel>


            <FloatingLabel
                controlId = "new_password"
                label = "New Password"
                className = "mb-3"
            >
                <Form.Control
                    type = "password"
                    name = "new_password"
                    placeholder = "New Password"
                    value = {passwords.new_password}
                    onChange = {handleChange}
                />
            </FloatingLabel>


            <FloatingLabel
                controlId = "confirm_password"
                label = "Confirm New Password"
                className = "mb-3"
            >
                <Form.Control
                    type = "password"
                    name = "confirm_password"
                    placeholder = "Confirm New Password"
                    value = {passwords.confirm_password}
                    onChange = {handleChange}
                    isInvalid = {
                        passwords.confirm_password &&
                        !passwordsMatch
                    }
                />

                <Form.Control.Feedback type = "invalid">
                    Passwords do not match.
                </Form.Control.Feedback>
            </FloatingLabel>


            <Button
                type = "submit"
                variant = "primary"
                disabled = {
                    !formComplete ||
                    !passwordsMatch
                }
            >
                Update Password
            </Button>

        </Form>
    )
}