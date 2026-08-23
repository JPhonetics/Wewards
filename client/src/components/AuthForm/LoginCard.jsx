import Card from 'react-bootstrap/Card';
import LoginForm from '../AuthForm/LoginForm';

function LoginCard({ setUser }) {

  return (
    <Card style={{ width: '18rem' }}>
      <Card.Body>
        <Card.Title>Login</Card.Title>
            <LoginForm setUser={setUser} />
      </Card.Body>
    </Card>
  );
}

export default LoginCard;