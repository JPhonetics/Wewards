import { useEffect, useState } from "react"

import { getBusinessItems } from "../../api/BusinessesAPI"


export default function BusinessItems({
    businessId,
}) {

    const [items, setItems] = useState([])

    // Store items when tab loads
    useEffect(() => {

        const loadItems = async () => {

            const businessItems = await getBusinessItems(
                businessId
            )

            if (businessItems) {
                setItems(businessItems)
            }
        }

        loadItems()

    }, [businessId])


    return (
        <>

            <h3>
                Items
            </h3>

            {items.map((item) => (

                <div key = {item.id}>

                    <strong>
                        {item.name}
                    </strong>

                    <p>
                        {item.description}
                    </p>

                    <p>
                        Status: {item.status_display}
                    </p>

                </div>

            ))}

        </>
    )
}