import Card from "react-bootstrap/Card"
import Button from "../../Button"


export default function RewardCard({
    reward,
}) {

    return (
        <Card className = "h-100">
            <Card.Body>

                <Card.Title>
                    {reward.name}
                </Card.Title>

                {reward.description && (
                    <Card.Text>
                        {reward.description}
                    </Card.Text>
                )}

                <div>
                    Required: {reward.amount_required}
                </div>

                {reward.qualifying_item_name && (
                    <div>
                        Qualifying Item: {reward.qualifying_item_name}
                    </div>
                )}

                {reward.earned_item_name && (
                    <div>
                        Reward Item: {reward.earned_item_name}
                    </div>
                )}

                {reward.discount_amount && (
                    <div>
                        Discount Amount: ${reward.discount_amount}
                    </div>
                )}

                {reward.discount_percentage && (
                    <div>
                        Discount Percentage: {reward.discount_percentage}%
                    </div>
                )}

                {reward.progress !== undefined && (
                    <div>
                        Progress: {reward.progress}
                    </div>
                )}

                <div className = "mb-3">
                    Eligible: {reward.eligible ? "Yes" : "No"}
                </div>

                {reward.eligible && (
                    <Button>
                        Redeem
                    </Button>
                )}

            </Card.Body>
        </Card>
    )
}