import { useOutletContext } from "react-router-dom"


export default function UserDashboard() {

    const { user } = useOutletContext()

    return (
        <>
        
            <h1>Welcome {user.first_name}</h1>

        </>
    )
}