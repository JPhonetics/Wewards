from django.urls import path

from apps.businesses.views.business import (
    BusinessRegister,
    BusinessDetail,
    BusinessStats
)
from apps.businesses.views.locations import (
    BusinessLocations,
    BusinessLocationDetail,
)
from apps.businesses.views.staff import (
    BusinessStaffInfo,
    BusinessStaffList,
)
from apps.businesses.views.items import (
    BusinessItems,
    BusinessItemDetail,
)


urlpatterns = [
    path('register/', BusinessRegister.as_view(), name = 'business_register'),
    path('staff/', BusinessStaffInfo.as_view(), name = 'business_staff'),
    path('<uuid:business_id>/', BusinessDetail.as_view(), name = 'business_detail'),
    path('<uuid:business_id>/stats/', BusinessStats.as_view(), name = 'business_stats'),
    path('<uuid:business_id>/locations/', BusinessLocations.as_view(), name = 'business_locations'),
    path('<uuid:business_id>/locations/<uuid:location_id>/', BusinessLocationDetail.as_view(), name = 'business_location_detail'),
    path('<uuid:business_id>/staff/', BusinessStaffList.as_view(), name = 'business_staff_list'),
    path('<uuid:business_id>/items/', BusinessItems.as_view(), name = 'business_items'),
    path('<uuid:business_id>/items/<uuid:item_id>/', BusinessItemDetail.as_view(), name = 'business_item_detail'),
]