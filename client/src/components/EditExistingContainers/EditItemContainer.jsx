import { useState } from "react"

import Card from "react-bootstrap/Card"
import Form from "react-bootstrap/Form"

import Button from "../Buttons"
import { BusinessItemForm } from "../Forms"

import { postBusinessItems } from "../../api/BusinessesAPI"


export default function AddItemContainer({
    businessId,
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

                    <Button
                        type = "submit"
                        disabled = {!itemComplete}
                    >
                        Add Item
                    </Button>

                </Form>

            </Card.Body>

        </Card>
    )
}