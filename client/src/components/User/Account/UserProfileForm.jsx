import { useState } from "react"
import Form from "react-bootstrap/Form"
import Button from "react-bootstrap/Button"
import FloatingLabel from "react-bootstrap/FloatingLabel"

import { updateUserProfile } from "../../../api/AccountsAPI"


export default function UserProfileForm({user, setUser}) {

    // Populate the form with the current database values
    const [profile, setProfile] = useState({
        first_name: user.first_name,
        last_name: user.last_name,
        email: user.email,
        phone_number: user.phone_number,
        country: user.country,
    })

    // Fields that have changed
    const hasChanges =
        profile.first_name !== user.first_name ||
        profile.last_name !== user.last_name ||
        profile.email !== user.email ||
        profile.phone_number !== user.phone_number ||
        profile.country !== user.country

    // If a field changes, update that value in profile state
    const handleChange = (event) => {
        const { name, value } = event.target

        setProfile((currentProfile) => ({
            ...currentProfile,
            [name]: value,
        }))
    }

    // Send the updated profile fields
    const handleSubmit = async (event) => {
        event.preventDefault()

        const updatedProfile = {}

        for (const field in profile) {
            if (profile[field] !== user[field]) {
                updatedProfile[field] = profile[field]
            }
        }

        const updatedUser = await updateUserProfile(
            updatedProfile
        )

        if (updatedUser) {
            setUser(updatedUser)
        }
    }

    return (
        <Form onSubmit = {handleSubmit}>

            <FloatingLabel
                controlId = "first_name"
                label = "First Name"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "first_name"
                    placeholder = "First Name"
                    value = {profile.first_name}
                    onChange = {handleChange}
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
                    value = {profile.last_name}
                    onChange = {handleChange}
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
                    value = {profile.email}
                    onChange = {handleChange}
                />
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
                    value = {profile.phone_number}
                    onChange = {handleChange}
                />
            </FloatingLabel>


            <FloatingLabel
                controlId = "country"
                label = "Country"
                className = "mb-3"
            >
                <Form.Control
                    type = "text"
                    name = "country"
                    placeholder = "Country"
                    value = {profile.country}
                    onChange = {handleChange}
                />
            </FloatingLabel>


            <Button
                type = "submit"
                variant = "primary"
                disabled = {!hasChanges}
            >
                Save Changes
            </Button>

        </Form>
    )
}