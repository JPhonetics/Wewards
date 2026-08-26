from django.urls import path

from apps.rewards.views.reward_programs import (
    RewardProgramTypesList,
    RewardProgramsList,
)
from apps.rewards.views.rewards import (
    RewardList,
)


urlpatterns = [
    path('program-types/', RewardProgramTypesList.as_view(), name = 'reward_program_types'),
    path('<uuid:business_id>/reward-programs/', RewardProgramsList.as_view(), name = 'reward_programs'),
    path('<uuid:business_id>/rewards/', RewardList.as_view(), name = 'rewards'),
]