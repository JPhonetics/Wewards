import { useEffect, useState } from "react"

import Button from "../Buttons"
import ListGroup from "react-bootstrap/ListGroup"

import { billingProducts } from "../../api/BillingAPI"


export default function BusinessBilling({
    businessId,
}) {

    const [billing, setBilling] = useState([])

    useEffect(() => {

        const loadBilling = async () => {

            const response = await billingProducts()

            if (response) {
                setBilling(response.products)
            }
        }

        loadBilling()

    }, [])

    return (

        <ListGroup>

            {billing.map((product) => (

                <ListGroup.Item
                    key = {product.id}
                >

                    <div>

                        <strong>
                            {product.name}
                        </strong>

                        {product.prices.map((price) => (

                            <div key = {price.id}>

                                <div>
                                    {price.name}
                                </div>

                                <div>
                                    {price.unit_amount}
                                </div>

                            </div>

                        ))}

                    </div>

                    <Button
                        type = "submit"
                    >
                        Subscribe
                    </Button>

                </ListGroup.Item>

            ))}

        </ListGroup>
    )
}