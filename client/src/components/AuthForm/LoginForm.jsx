import { useNavigate } from 'react-router-dom'
import { useState } from 'react';
import { userLogin } from '../../utilities';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';


const LoginForm = ({setUser}) => {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault()

        const loggedInUser = await userLogin(username, password)
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

                <Button variant="primary" type="submit">
                    Login
                </Button>
            </Form>
        </>
    )
}

export default LoginForm