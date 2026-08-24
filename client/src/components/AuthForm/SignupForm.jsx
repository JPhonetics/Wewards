import { useNavigate } from 'react-router-dom'
import { useState } from 'react';
import { userConfirmation, userSignup } from '../../utilities';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function SignupForm({setUser}) {

    const [signupEmail, setSignupEmail] = useState('')
    const [signupPassword, setSignupPassword] = useState('')
    const navigate = useNavigate()

    const handleSignup = async (e) => {
        e.preventDefault()

        const registerUser = await userSignup(signupEmail, signupPassword)
        if (!registerUser) return

        const registeredUser = await userConfirmation()
        if (!registeredUser) return

        setUser(registeredUser)
        setSignupEmail('')
        setSignupPassword('')
        navigate('/user/dashboard')
    }

    return (

        <Form onSubmit={handleSignup}>
            <Form.Group className="mb-3" controlId="formSignupEmail">
                <Form.Control 
                    type = "email" 
                    placeholder = "Email" 
                    value = {signupEmail}
                    onChange = {(e) => setSignupEmail(e.target.value)}
                    required
                />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formSignupPassword">
                <Form.Control 
                    type = "password" 
                    placeholder = "Password" 
                    value = {signupPassword}
                    onChange = {(e) => setSignupPassword(e.target.value)}
                    required
                />
            </Form.Group>

            <Button variant="primary" type="submit">
                Sign Up
            </Button>
        </Form>

    )

}

export default SignupForm