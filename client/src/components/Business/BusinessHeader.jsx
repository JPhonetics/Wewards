import Card from "react-bootstrap/Card"


export default function BusinessHeader({
    business,
    businessStaff,
}) {

    return (

        <Card className = "mb-4">

            <Card.Body>

                <div className = "d-flex align-items-center justify-content-center">

                    <div
                        className = "d-flex align-items-center justify-content-center me-4"
                        style = {{
                            width: "100px",
                            height: "100px",
                        }}
                    >

                        {business.logo ? (
                            <img
                                src = {business.logo}
                                alt = {`${business.name} logo`}
                                className = "img-fluid"
                                style = {{
                                    maxHeight: "100px",
                                    maxWidth: "100px",
                                }}
                            />
                        ) : (
                            <strong>
                                Wewards
                            </strong>
                        )}

                    </div>

                    <div className = "text-center">

                        <h1 className = "mb-1">
                            {business.name}
                        </h1>

                        <p className = "mb-1">
                            {business.industry}
                        </p>

                        <p className = "mb-0">
                            Role: {businessStaff.role_display}
                        </p>

                    </div>

                </div>

            </Card.Body>

        </Card>
    )
}