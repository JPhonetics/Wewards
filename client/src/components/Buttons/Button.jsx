import BootstrapButton from "react-bootstrap/Button"


export default function Button({
    children,
    variant = "primary",
    ...props
}) {

    return (

        <BootstrapButton
            variant = {variant}
            {...props}
        >
            {children}
        </BootstrapButton>
    )
}