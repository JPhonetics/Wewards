import { useEffect, useState } from "react"
import { Outlet, useLoaderData } from "react-router-dom"

import Heading from "./components/Heading/Heading"
import NavBar from "./components/NavBar"

import { getBusinessStaff } from "./api/BusinessesAPI"


export default function App() {

  // Store authenticated user data
  const [user, setUser] = useState(useLoaderData())

  // Store businesses the user belongs to
  const [businessStaff, setBusinessStaff] = useState([])

  // Store business staff when page loads
  useEffect(() => {

    const loadBusinessStaff = async () => {

      // Clear business data if no user is logged in
      if (!user) {
        setBusinessStaff([])
        return
      }

      // Call the API and store business staff if returned
      const staff = await getBusinessStaff()

      if (staff) {
        setBusinessStaff(staff)
      }
    }

    loadBusinessStaff()

  }, [user])


  return (
    <>
      <Heading />

      <NavBar
        user = {user}
        setUser = {setUser}
        businessStaff = {businessStaff}
        setBusinessStaff = {setBusinessStaff}
      />

      <Outlet
        context = {{
          user,
          setUser,
          businessStaff,
          setBusinessStaff,
        }}
      />
    </>
  )
}