import Button from "react-bootstrap/Button"


export default function BusinessInfo({business}) {

    return (
        <>

            <div className = "d-flex justify-content-end align-items-center mb-3">

                <Button
                    variant = "primary"
                >
                    Edit
                </Button>

            </div>

            <p>
                <strong>
                    Name:
                </strong>
                {" "}
                {business.name}
            </p>

            <p>
                <strong>
                    Industry:
                </strong>
                {" "}
                {business.industry}
            </p>

            <p>
                <strong>
                    Email:
                </strong>
                {" "}
                {business.email}
            </p>

            <p>
                <strong>
                    Phone Number:
                </strong>
                {" "}
                {business.phone_number}
            </p>

            <p>
                <strong>
                    Website:
                </strong>
                {" "}
                {business.website || "Not provided"}
            </p>

        </>
    )
}