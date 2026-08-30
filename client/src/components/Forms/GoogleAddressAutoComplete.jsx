import { useEffect, useRef } from "react"

import { loadPlacesLibrary } from "../../api/GoogleMaps"


export default function GoogleAddressAutoComplete({
    setLocation,
}) {

    const autoCompleteRef = useRef(null)


    useEffect(() => {

        const loadGoogleAutoComplete = async () => {

            // Request needed libraries.
            // Load Google's Places library
            const { PlaceAutocompleteElement } =
                await loadPlacesLibrary()

            // Create the input HTML element, and append it.
            // Create Google's autocomplete search box
            const autoComplete = new PlaceAutocompleteElement()

            autoComplete.placeholder = "Search Address"

            // Put Google's search box inside our React div
            autoCompleteRef.current.appendChild(
                autoComplete
            )

            // Add the gmp-select listener, and display the results.
            // Runs when the user selects an address
            autoComplete.addEventListener(
                "gmp-select",
                async ({ placePrediction }) => {

                    const place = placePrediction.toPlace()

                    // Get the address pieces from Google
                    await place.fetchFields({
                        fields: [
                            "addressComponents",
                            "location",
                            "timeZone",
                        ],
                    })

                    const timezone = place.timeZone?.id || ""

                    let streetNumber = ""
                    let street = ""
                    let city = ""
                    let stateRegion = ""
                    let postalCode = ""
                    let country = ""

                    // Break Google's address into our form fields
                    for (const component of place.addressComponents) {

                        if (component.types.includes("street_number")) {
                            streetNumber = component.longText
                        }

                        if (component.types.includes("route")) {
                            street = component.longText
                        }

                        if (
                            component.types.includes("locality") ||
                            component.types.includes("postal_town")
                        ) {
                            city = component.longText
                        }

                        if (component.types.includes("administrative_area_level_1")) {
                            stateRegion = component.longText
                        }

                        if (component.types.includes("postal_code")) {
                            postalCode = component.longText
                        }

                        if (component.types.includes("country")) {
                            country = component.shortText
                        }
                    }

                    // // Get the selected address coordinates
                    // const latitude = place.location.lat()
                    // const longitude = place.location.lng()

                    // // Use the coordinates to get the correct timezone
                    // const timezone = await getTimeZone(
                    //     latitude,
                    //     longitude,
                    // )

                    // console.log("Timezone:", timezone)

                    // Fill our existing BusinessLocation form
                    setLocation((currentLocation) => ({
                        ...currentLocation,
                        address_line_1: `${streetNumber} ${street}`.trim(),
                        city: city,
                        state_region: stateRegion,
                        postal_code: postalCode,
                        country: country,
                        timezone: timezone,
                    }))
                }
            )
        }

        loadGoogleAutoComplete()

    }, [setLocation])


    return (
        <div
            ref = {autoCompleteRef}
            className = "form-control p-0"
        />
    )
}