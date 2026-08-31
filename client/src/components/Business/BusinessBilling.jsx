import { useEffect, useState } from "react"

import Button from "../Buttons"
import ListGroup from "react-bootstrap/ListGroup"

import {
    billingProducts,
    subscribeBusiness,
} from "../../api/BillingAPI"


export default function BusinessBilling({
    businessId,
}) {

    const [billing, setBilling] = useState([])

    useEffect(() => {

        const loadBilling = async () => {

            // Get all active Stripe products and prices
            const response = await billingProducts()

            if (response) {
                setBilling(response.products)
            }
        }

        loadBilling()

    }, [])


    const handleSubscribe = async (priceId) => {

        // Send the selected Stripe Price ID to Django
        const response = await subscribeBusiness(
            businessId,
            priceId,
        )

        // Django returns the Stripe Checkout URL
        // Redirect the browser to Stripe
        window.location.href = response.checkout_url
    }


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

                                <Button
                                    type = "button"
                                    onClick = {() => handleSubscribe(price.id)}
                                >
                                    Subscribe
                                </Button>

                            </div>

                        ))}

                    </div>

                </ListGroup.Item>

            ))}

        </ListGroup>
    )
}