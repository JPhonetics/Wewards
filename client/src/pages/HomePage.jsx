import { Link, useOutletContext } from "react-router-dom"
import Button from "react-bootstrap/Button"


export default function HomePage() {

    const { user } = useOutletContext()

    return (
        <>
            <h1>Home Page</h1>

            {user && (
                <Button
                    as = {Link}
                    to = "/user/dashboard"
                    variant = "primary"
                >
                    User Dashboard
                </Button>
            )}

        </>
    )
}