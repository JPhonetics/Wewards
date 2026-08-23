import Card from 'react-bootstrap/Card';
import RegisterForm from '../AuthForm/RegisterForm';

function LoginCard({ setUser }) {

  return (
    <Card style={{ width: '18rem' }}>
      <Card.Body>
        <Card.Title>Login</Card.Title>
            <RegisterForm setUser={setUser} />
      </Card.Body>
    </Card>
  );
}

export default LoginCard;