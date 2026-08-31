import Card from "react-bootstrap/Card"


export default function BusinessStatsCard({
    count,
    label,
}) {

    return (

        <Card className = "h-100 text-center">

            <Card.Body>

                <Card.Title
                    as = "h2"
                    className = "mb-1"
                >
                    {count}
                </Card.Title>

                <Card.Text className = "mb-0">
                    {label}
                </Card.Text>

            </Card.Body>

        </Card>
    )
}