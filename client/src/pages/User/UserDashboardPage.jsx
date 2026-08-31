import { useOutletContext } from "react-router-dom"
import RewardsContainer from "../../components/User/Rewards/RewardsContainer"


export default function UserDashboard() {

    const { user } = useOutletContext()

    return (
        <>
            <h1>Welcome {user.first_name}</h1>

            <RewardsContainer />
        </>
    )
}