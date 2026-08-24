import { Link, useNavigate } from 'react-router-dom'
import { useState } from 'react';
import { userConfirmation, userLogin } from '../../utilities';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function LoginForm({setUser}) {

    const [loginUsername, setLoginUsername] = useState('')
    const [loginPassword, setLoginPassword] = useState('')
    const navigate = useNavigate()

    const handleLogin = async (e) => {
        e.preventDefault()

        const logInUser = await userLogin(loginUsername, loginPassword)
        if (!logInUser) return

        const loggedInUser = await userConfirmation()
        if (!loggedInUser) return

        setUser(loggedInUser)
        setLoginUsername('')
        setLoginPassword('')
        navigate('/user/dashboard')
    }

    return (

        <Form onSubmit={handleLogin}>
            <Form.Group className="mb-3" controlId="formLoginUsername">
                <Form.Control 
                    type = "text" 
                    placeholder = "Email or Phone Number" 
                    value = {loginUsername}
                    onChange = {(e) => setLoginUsername(e.target.value)}
                    required
                />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formLoginPassword">
                <Form.Control 
                    type = "password" 
                    placeholder = "Password" 
                    value = {loginPassword}
                    onChange = {(e) => setLoginPassword(e.target.value)}
                    required
                />
            </Form.Group>

            <Form.Group>
                <Link to="/forgot-password" className="formForgotPassword">
                    Forgot password?
                </Link>
            </Form.Group>

            {/* <Form.Group as={Row} className="mb-3" controlId="formRememberMe">
                <Col sm={{ span: 10, offset: 2 }}>
                    <Form.Check label="Remember me" />
                </Col>
            </Form.Group> */}

            <Button variant="primary" type="submit">
                Login
            </Button>
        </Form>

    )

}

export default LoginForm