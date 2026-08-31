import { useOutletContext } from "react-router-dom"

import {
    UserProfileCard,
    UpdatePasswordCard
} from "../../components/User"


export default function UserProfilePage() {

    const { user, setUser } = useOutletContext()

    return (
        <>
            <UserProfileCard
                user = {user}
                setUser = {setUser}
            />
            <UpdatePasswordCard />
        </>
    )
}