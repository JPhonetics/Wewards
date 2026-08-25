import { Link } from "react-router-dom"


export default function UserDashboard() {

    return (
        <>
        
            <h1>User Dashboard</h1>

            <Link to = "/user/profile">
                Profile
            </Link>

        </>
    )
}