import { useNavigate } from "react-router-dom"
import { useState } from "react"

import Button from "react-bootstrap/Button"
import FloatingLabel from "react-bootstrap/FloatingLabel"
import Form from "react-bootstrap/Form"

import {
    userConfirmation,
    userSignup
} from "../../api/AccountsAPI"


function SignupForm({ setUser }) {

    const [user, setUserForm] = useState({
        first_name: "",
        last_name: "",
        email: "",
        phone_number: "",
        country: "",
        password: "",
        confirm_password: "",
    })

    const [termsAccepted, setTermsAccepted] = useState(false)

    const navigate = useNavigate()

    // Update the matching user field
    const handleChange = (event) => {
        const { name, value } = event.target

        setUserForm((currentUser) => ({
            ...currentUser,
            [name]: value,
        }))
    }

    // Password and confirmation must match
    const passwordsMatch =
        user.password === user.confirm_password

    // Require all fields before allowing submit
    const formComplete =
        user.first_name &&
        user.last_name &&
        user.email &&
        user.phone_number &&
        user.country &&
        user.password &&
        user.confirm_password

    const handleSignup = async (event) => {
        event.preventDefault()

        if (!passwordsMatch || !termsAccepted) {
            return
        }

        const signupUser = {
            first_name: user.first_name,
            last_name: user.last_name,
            email: user.email,
            phone_number: user.phone_number,
            country: user.country,
            password: user.password,
        }

        const registerUser = await userSignup(signupUser)
        console.log(registerUser)
        if (!registerUser) return

        const registeredUser = await userConfirmation()
        console.log(registeredUser)
        if (!registeredUser) return

        setUser(registeredUser)

        setUserForm({
            first_name: "",
            last_name: "",
            email: "",
            phone_number: "",
            country: "",
            password: "",
            confirm_password: "",
        })

        setTermsAccepted(false)
        navigate("/user/dashboard")
    }


    return (

        <Form onSubmit = {handleSignup}>

            <FloatingLabel
                controlId = "first_name"
                label = "First Name"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "first_name"
                    placeholder = "First Name"
                    value = {user.first_name}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "last_name"
                label = "Last Name"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "last_name"
                    placeholder = "Last Name"
                    value = {user.last_name}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "email"
                label = "Email"
                className = "mb-3"
            >
                <Form.Control
                    type = "email"
                    name = "email"
                    placeholder = "Email"
                    value = {user.email}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "country"
                label = "Country"
                className = "mb-3"
            >
                <Form.Select
                    name = "country"
                    value = {user.country}
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
                controlId = "phone_number"
                label = "Phone Number"
                className = "mb-3"
            >
                <Form.Control
                    type = "tel"
                    name = "phone_number"
                    placeholder = "Phone Number"
                    value = {user.phone_number}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "password"
                label = "Password"
                className = "mb-3"
            >
                <Form.Control
                    type = "password"
                    name = "password"
                    placeholder = "Password"
                    value = {user.password}
                    onChange = {handleChange}
                    required
                />
            </FloatingLabel>

            <FloatingLabel
                controlId = "confirm_password"
                label = "Confirm Password"
                className = "mb-3"
            >
                <Form.Control
                    type = "password"
                    name = "confirm_password"
                    placeholder = "Confirm Password"
                    value = {user.confirm_password}
                    onChange = {handleChange}
                    isInvalid = {
                        user.confirm_password &&
                        !passwordsMatch
                    }
                    required
                />

                <Form.Control.Feedback type = "invalid">
                    Passwords do not match.
                </Form.Control.Feedback>
            </FloatingLabel>

            <Form.Check
                type = "checkbox"
                id = "terms"
                className = "mb-3"
                checked = {termsAccepted}
                onChange = {(event) =>
                    setTermsAccepted(event.target.checked)
                }
                label = {
                    <>
                        I agree to the Terms of Service and Privacy Policy.
                    </>
                }
            />

            <Button
                variant = "primary"
                type = "submit"
                disabled = {
                    !formComplete ||
                    !passwordsMatch ||
                    !termsAccepted
                }
            >
                Sign Up
            </Button>

        </Form>

    )
}

export default SignupForm