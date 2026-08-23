import { Link, useNavigate } from 'react-router-dom'
import { useState } from 'react';
import { userConfirmation, userLogin, userRegistration } from '../../utilities';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';

function RegisterForm({setUser}) {

    const [loginUsername, setLoginUsername] = useState('')
    const [loginPassword, setLoginPassword] = useState('')
    const [registrationEmail, setRegistrationEmail] = useState('')
    const [registrationPassword, setRegistrationPassword] = useState('')
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
        navigate('/home')
    }

    const handleRegistration = async (e) => {
        e.preventDefault()

        const registerUser = await userRegistration(registrationEmail, registrationPassword)
        if (!registerUser) return

        const registeredUser = await userConfirmation()
        if (!registeredUser) return

        setUser(registeredUser)
        setRegistrationEmail('')
        setRegistrationPassword('')
        navigate('/home')
    }

    return (
        <Tabs
        defaultActiveKey="login"
        id="justify-tab-example"
        className="mb-3"
        justify
        >
        <Tab eventKey="login" title="Login">

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

        </Tab>
            <Tab eventKey="register" title="Join">

                <Form onSubmit={handleRegistration}>
                    <Form.Group className="mb-3" controlId="formRegisterEmail">
                        <Form.Control 
                            type = "email" 
                            placeholder = "Email" 
                            value = {registrationEmail}
                            onChange = {(e) => setRegistrationEmail(e.target.value)}
                            required
                        />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="formRegisterPassword">
                        <Form.Control 
                            type = "password" 
                            placeholder = "Password" 
                            value = {registrationPassword}
                            onChange = {(e) => setRegistrationPassword(e.target.value)}
                            required
                        />
                    </Form.Group>

                    <Button variant="primary" type="submit">
                        Submit
                    </Button>
                </Form>

            </Tab>

        </Tabs>
    );
    }

export default RegisterForm