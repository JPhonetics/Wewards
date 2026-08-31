import { useEffect, useState } from "react"

import Alert from "react-bootstrap/Alert"

import { getBusinessBilling } from "../../api/BillingAPI"


export default function BusinessOverview({
    businessId,
}) {

    const [billing, setBilling] = useState(null)

    useEffect(() => {

        const loadBilling = async () => {

            const response = await getBusinessBilling(
                businessId
            )
            
            console.log(response)
            
            if (response) {
                setBilling(response)
            }
        }

        loadBilling()

    }, [businessId])

    return (

        <div>

            {billing?.status === "trialing" && (

                <Alert variant = "info">

                    <Alert.Heading>
                        Free Trial
                    </Alert.Heading>

                    <div>
                        Your Wewards trial is active.
                    </div>

                    <div>
                        Trial ends: {billing.trial_end}
                    </div>

                    <div>
                        Thank you for taking the time and giving Wewards a try! Your feedback is important to us. Please take a moment and let us know how we can improve.
                    </div>

                </Alert>

            )}

            Overview

        </div>
    )
}