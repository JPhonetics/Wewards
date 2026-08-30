import { Link, useNavigate } from "react-router-dom"

import Container from "react-bootstrap/Container"
import Nav from "react-bootstrap/Nav"
import Navbar from "react-bootstrap/Navbar"
import NavDropdown from "react-bootstrap/NavDropdown"

import { userLogOut } from "../../api/AccountsAPI"


function NavBar({
  user,
  setUser,
  businessStaff,
  setBusinessStaff,
}) {

  const navigate = useNavigate()


  const handleLogOut = async () => {

    await userLogOut()

    setUser(null)
    setBusinessStaff([])

    navigate("/")
  }


  return (

    <Navbar
      bg = "primary"
      data-bs-theme = "dark"
      expand = "lg"
    >

      <Container>
        <Navbar.Brand
          as = {Link}
          to = "/"
          expand = "lg"
        >
          Wewards
        </Navbar.Brand>

        <Navbar.Toggle />

        <Navbar.Collapse>
          <Nav>

            <Nav.Link
              as = {Link}
              to = "/"
            >
              How It Works?
            </Nav.Link>

            <Nav.Link
              as = {Link}
              to = "/business/register"
            >
              For Business
            </Nav.Link>

          </Nav>

          <Nav className = "ms-auto">

            {user && businessStaff.length > 0 && (

              <NavDropdown
                title = "Business"
                align = "end"
              >

                {businessStaff.map((staff) => (

                  <NavDropdown.Item
                    key = {staff.id}
                    as = {Link}
                    to = {`/business/${staff.business.id}`}
                  >
                    {staff.business.name}
                  </NavDropdown.Item>

                ))}

                <NavDropdown.Divider />

                <NavDropdown.Item
                  as = {Link}
                  to = "/business/dashboard"
                >
                  All Businesses
                </NavDropdown.Item>

              </NavDropdown>

            )}


            {user ? (

              <NavDropdown
                title = {user.first_name}
                align = "end"
              >

                <NavDropdown.Item
                  as = {Link}
                  to = "/user/dashboard"
                >
                  User Dashboard
                </NavDropdown.Item>

                <NavDropdown.Item
                  as = {Link}
                  to = "/user/profile"
                >
                  Profile
                </NavDropdown.Item>

                <NavDropdown.Divider />

                <NavDropdown.Item
                  onClick = {handleLogOut}
                >
                  Logout
                </NavDropdown.Item>

              </NavDropdown>

            ) : (

              <Nav.Link
                as = {Link}
                to = "/login"
              >
                Login
              </Nav.Link>

            )}

          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  )
}


export default NavBar