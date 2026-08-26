import { useEffect, useState } from "react"

import Button from "react-bootstrap/Button"
import ListGroup from "react-bootstrap/ListGroup"

import {
    deleteBusinessItem,
    getBusinessItems,
} from "../../api/BusinessesAPI"


export default function BusinessItems({
    businessId,
    itemRefresh,
}) {

    const [items, setItems] = useState([])


    useEffect(() => {

        const loadItems = async () => {

            const response = await getBusinessItems(
                businessId
            )

            if (response) {
                setItems(response)
            }
        }

        loadItems()

    }, [
        businessId,
        itemRefresh
    ])


    const handleDelete = async (itemId) => {

        const response = await deleteBusinessItem(
            businessId,
            itemId
        )

        if (response) {

            setItems((currentItems) =>
                currentItems.filter(
                    (item) => item.id !== itemId
                )
            )
        }
    }


    return (

        <ListGroup>

            {items.map((item) => (

                <ListGroup.Item
                    key = {item.id}
                    className = "d-flex justify-content-between align-items-center"
                >

                    <div>

                        <strong>
                            {item.name}
                        </strong>

                        <div>
                            {item.status_display}
                        </div>

                    </div>

                    <Button
                        variant = "danger"
                        onClick = {
                            () => handleDelete(item.id)
                        }
                    >
                        Delete
                    </Button>

                </ListGroup.Item>

            ))}

        </ListGroup>
    )
}