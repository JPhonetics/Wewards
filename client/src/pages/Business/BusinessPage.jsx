import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"

import {
    getBusiness,
    getBusinessStats
} from "../../api/BusinessesAPI"

import {
    BusinessHeader,
    BusinessManagementCard,
    BusinessStats,
} from "../../components/Business"


export default function BusinessPage() {

    // Get business ID from the URL
    const { businessId } = useParams()

    // Store businesses the user belongs to
    const [businessStaff, setBusinessStaff] = useState(null)

    // Store selected business stats
    const [stats, setStats] = useState(null)

    // Store business when page loads
    useEffect(() => {

        const loadBusiness = async () => {

            const staff = await getBusiness(
                businessId
            )

            if (staff) {
                setBusinessStaff(staff)
            }

            const businessStats = await getBusinessStats(
                businessId
            )

            if (businessStats) {
                setStats(businessStats)
            }
        }

        loadBusiness()

    }, [businessId])


    if (!businessStaff || !stats) {
        return null
    }

    const business = businessStaff.business


    return (
        <>

            <BusinessHeader
                business = {business}
                businessStaff = {businessStaff}
            />

            <BusinessStats
                stats = {stats}
            />

            <BusinessManagementCard
                business = {business}
                businessId = {businessId}
                businessStaff = {businessStaff}
                setBusinessStaff = {setBusinessStaff}
            />

        </>
    )
}