from django.urls import path
from apps.businesses.views import (
    BusinessRegister,
    BusinessStaffInfo,
    BusinessDetail,
    BusinessStats,
    BusinessLocations,
    BusinessStaffList,
    BusinessItems,
)

urlpatterns = [
    path('register/', BusinessRegister.as_view(), name = 'business_register'),
    path('staff/', BusinessStaffInfo.as_view(), name = 'business_staff'),
    path('<uuid:business_id>/', BusinessDetail.as_view(), name = 'business_detail'),
    path('<uuid:business_id>/stats/', BusinessStats.as_view(), name = 'business_stats'),
    path('<uuid:business_id>/locations/', BusinessLocations.as_view(), name = 'business_locations'),
    path('<uuid:business_id>/staff/', BusinessStaffList.as_view(), name = 'business_staff_list'),
    path('<uuid:business_id>/items/', BusinessItems.as_view(), name = 'business_items'),
]