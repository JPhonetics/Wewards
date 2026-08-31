import LoginForm from './LoginForm';
import RegistrationForm from './SignupForm';
import Card from 'react-bootstrap/Card';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';


function LoginCard({setUser}) {

  return (
    <Card style = {{ width: '18rem' }}>
      <Card.Img variant="top" />
      <Card.Body>

        <Tabs
          defaultActiveKey = "login"
          id = "justify-tab-example"
          className = "mb-3"
          justify
        >

          <Tab eventKey="login" title="Login">
            <LoginForm setUser = {setUser}/>
          </Tab>

          <Tab eventKey="signup" title="Signup">
            <RegistrationForm setUser = {setUser}/>
          </Tab>

        </Tabs>

      </Card.Body>
    </Card>

  );
}

export default LoginCard