from rest_framework.serializers import (
    ModelSerializer,
    CharField,
)
from apps.rewards.models import (
    RewardProgramType,
    RewardProgram,
    RewardProgramLocation,
    Reward,
    RewardLocation,
)


class RewardProgramTypeSerializer(ModelSerializer):

    class Meta:
        model = RewardProgramType
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'modified_date': {'read_only': True},
        }


class RewardProgramSerializer(ModelSerializer):

    program_type_name = CharField(
        source = 'program_type.name',
        read_only = True
    )

    class Meta:
        model = RewardProgram
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'business': {'read_only': True},
            'created_date': {'read_only': True},
            'modified_date': {'read_only': True},
        }


class RewardProgramLocationSerializer(ModelSerializer):

    class Meta:
        model = RewardProgramLocation
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'modified_date': {'read_only': True},
        }


class RewardSerializer(ModelSerializer):

    class Meta:
        model = Reward
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'modified_date': {'read_only': True},
        }


class RewardLocationSerializer(ModelSerializer):

    class Meta:
        model = RewardLocation
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'modified_date': {'read_only': True},
        }