import { Link, useNavigate } from 'react-router-dom';
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

import { userLogOut } from "../../utilities";


function NavBar({ user, setUser }) {

  const navigate = useNavigate()

  const handleLogOut = async () => {
    await userLogOut()
    setUser(null)
    navigate('/')
  }

  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">Home</Nav.Link>
            <Nav.Link as={Link} to="/">How It Works?</Nav.Link>
            <Nav.Link as={Link} to="/">For Business</Nav.Link>
          </Nav>

           {user && (
              <Button
                  variant="outline-light"
                  onClick={handleLogOut}
              >
                  Logout
              </Button>
          )}
        </Container>
      </Navbar>
    </>
  );
}

export default NavBar;