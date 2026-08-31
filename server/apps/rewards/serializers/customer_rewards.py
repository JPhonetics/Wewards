from rest_framework.serializers import (
    Serializer,
    CharField,
    UUIDField,
    DecimalField,
    IntegerField,
    BooleanField,
)


class CustomerRewardSerializer(Serializer):

    id = UUIDField(
        source = 'reward.id',
        read_only = True
    )
    name = CharField(
        source = 'reward.name',
        read_only = True
    )
    reward_type = CharField(
        source = 'reward.reward_type',
        read_only = True
    )
    description = CharField(
        source = 'reward.description',
        read_only = True
    )
    amount_required = IntegerField(
        source = 'reward.amount_required',
        read_only = True
    )
    discount_amount = DecimalField(
        source = 'reward.discount_amount',
        max_digits = 5,
        decimal_places = 2,
        allow_null = True,
        read_only = True
    )
    discount_percentage = DecimalField(
        source = 'reward.discount_percentage',
        max_digits = 5,
        decimal_places = 2,
        allow_null = True,
        read_only = True
    )
    status = CharField(
        source = 'reward.status',
        read_only = True
    )
    end_date = CharField(
        source = 'reward.end_date',
        allow_null = True,
        read_only = True
    )
    qualifying_item = UUIDField(
        source = 'reward.qualifying_item.id',
        allow_null = True,
        read_only = True
    )
    qualifying_item_name = CharField(
        source = 'reward.qualifying_item.name',
        allow_null = True,
        read_only = True
    )
    earned_item = UUIDField(
        source = 'reward.earned_item.id',
        allow_null = True,
        read_only = True
    )
    earned_item_name = CharField(
        source = 'reward.earned_item.name',
        allow_null = True,
        read_only = True
    )
    eligible = BooleanField()
    progress = IntegerField(
        required = False
    )


class CustomerRewardProgramSerializer(Serializer):

    reward_program_id = UUIDField(
        source = 'reward_program.id',
        read_only = True
    )
    reward_program_name = CharField(
        source = 'reward_program.name',
        read_only = True
    )
    program_type = CharField(
        source = 'reward_program.program_type.name',
        read_only = True
    )
    balance = DecimalField(
        max_digits = 12,
        decimal_places = 2,
        required = False
    )
    rewards = CustomerRewardSerializer(
        many = True,
        required = False
    )


class CustomerRewardsSerializer(Serializer):

    business_id = UUIDField(
        source = 'business.id',
        read_only = True
    )
    business_name = CharField(
        source = 'business.name',
        read_only = True
    )
    reward_programs = CustomerRewardProgramSerializer(
        many = True
    )