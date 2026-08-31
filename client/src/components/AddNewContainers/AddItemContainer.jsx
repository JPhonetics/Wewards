import { useState } from "react"

import Card from "react-bootstrap/Card"
import Form from "react-bootstrap/Form"

import Button from "../Buttons"

import {
    BusinessItemForm
} from "../Forms"

import {
    postBusinessItems
} from "../../api/BusinessesAPI"


export default function AddItemContainer({
    businessId,
    setShowAddItem,
    setItemRefresh,
}) {

    const [item, setItem] = useState({
        name: "",
        description: "",
        status: "draft",
    })

    const itemComplete =
        item.name &&
        item.status


    const handleSubmit = async (event) => {
        event.preventDefault()

        const response = await postBusinessItems(
            businessId,
            item
        )

        if (response) {

            setItem({
                name: "",
                description: "",
                status: "draft",
            })

            setItemRefresh(
                (currentRefresh) =>
                    currentRefresh + 1
            )

            setShowAddItem(false)
        }
    }


    return (

        <Card className = "mb-4">

            <Card.Body>

                <Card.Title
                    as = "h3"
                    className = "mb-4"
                >
                    Add Item
                </Card.Title>

                <Form onSubmit = {handleSubmit}>

                    <BusinessItemForm
                        item = {item}
                        setItem = {setItem}
                    />

                    <div className = "d-flex justify-content-between">

                        <Button
                            type = "button"
                            variant = "secondary"
                            onClick = {
                                () => setShowAddItem(false)
                            }
                        >
                            Cancel
                        </Button>

                        <Button
                            type = "submit"
                            disabled = {!itemComplete}
                        >
                            Add Item
                        </Button>

                    </div>

                </Form>

            </Card.Body>

        </Card>
    )
}