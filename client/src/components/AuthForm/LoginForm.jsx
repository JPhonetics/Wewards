import { Link, useNavigate } from 'react-router-dom'
import { useState } from 'react';
import { userLogin, userConfirmation } from '../../utilities';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';


const LoginForm = ({setUser}) => {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault()

        const logInUser = await userLogin(username, password)
        if (!logInUser) return

        const loggedInUser = await userConfirmation()
        if (!loggedInUser) return

        setUser(loggedInUser)
        setUsername('')
        setPassword('')
        navigate('/home')
    }

    return (
        <>
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="formUsername">
                    <Form.Control 
                        type = "text" 
                        placeholder = "Email or Phone Number" 
                        value = {username}
                        onChange = {(e) => setUsername(e.target.value)}
                        required
                    />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword">
                    <Form.Control 
                        type = "password" 
                        placeholder = "Password" 
                        value = {password}
                        onChange = {(e) => setPassword(e.target.value)}
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
        </>
    )
}

export default LoginForm