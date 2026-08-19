from django.contrib import admin
from apps.rewards.forms import *

## Reward Program Type Portal
class RewardProgramTypeAdmin(admin.ModelAdmin):

    add_form = RewardProgramTypeAddForm
    form = RewardProgramTypeForm

    model = RewardProgramType
    
    list_display = [
        'name',
        'description',
    ]
    
    ordering = [
        'name',
    ]
    
    readonly_fields = [
        'id',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                )
            },
        ),
        (
            'Reward Program Type',
            {
                'fields': (
                    'name',
                    'description',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Reward Program Type',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'name',
                    'description',
                ),
            },
        ),
    )
    
    
## Reward Program Portal
class RewardProgramAdmin(admin.ModelAdmin):

    add_form = RewardProgramAddForm
    form = RewardProgramForm

    model = RewardProgram
    
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'name',
        'status',
        'start_date',
        'end_date',
    ]
    
    list_filter = [
        'status',
    ]
    
    search_fields = [
        'name',
    ]
    
    ordering = [
        'name',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                )
            },
        ),
        (
            'Reward Program Information',
            {
                'fields': (
                    'start_date',
                    'name',
                    'description',
                )
            },
        ),
        (
            'Status',
            {
                'fields': (
                    'status',
                    'end_date',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Reward Program',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'business',
                    'program_type',
                    'start_date',
                    'name',
                    'description',
                    'status',
                ),
            },
        ),
    )
    
    
## Reward Location Admin Portal
class RewardProgramLocationAdmin(admin.ModelAdmin):

    add_form = RewardProgramLocationAddForm
    form = RewardProgramLocationForm

    model = RewardProgramLocation
    
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'location',
        'reward_program',
    ]
    
    search_fields = [
        'location',
        'reward_program',
    ]
    
    ordering = [
        'location',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                )
            },
        ),
        (
            'Reward Program Location Information',
            {
                'fields': (
                    'location',
                    'reward_program',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Reward Program Location',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'location',
                    'reward_program',
                ),
            },
        ),
    )
    
    
## Reward Admin Portal
class RewardAdmin(admin.ModelAdmin):

    add_form = RewardAddForm
    form = RewardForm

    model = Reward
    
    # Drop down to select primary records
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'name',
        'qualifying_item',
        'earned_item',
        'amount_required',
        'discount_amount',
        'discount_percentage',
        'status',
    ]
    
    list_filter = [
        'status',
    ]
    
    search_fields = [
        'name',
        'qualifying_item',
        'earned_item',
    ]
    
    ordering = [
        'name',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                )
            },
        ),
        (
            'Reward Information',
            {
                'fields': (
                    'name',
                    'description',
                    'qualifying_item',
                    'earned_item',
                    'amount_required',
                    'discount_amount',
                    'discount_percentage',
                )
            },
        ),
        (
            'Status',
            {
                'fields': (
                    'status',
                    'end_date',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Reward',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'reward_program',
                    'name',
                    'description',
                    'qualifying_item',
                    'earned_item',
                    'amount_required',
                    'discount_amount',
                    'discount_percentage'
                ),
            },
        ),
    )
    
    
## Reward Location Admin Portal
class RewardLocationAdmin(admin.ModelAdmin):

    add_form = RewardLocationAddForm
    form = RewardLocationForm

    model = RewardLocation
    
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'location',
        'reward',
    ]
    
    search_fields = [
        'location',
        'reward',
    ]
    
    ordering = [
        'location',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                )
            },
        ),
        (
            'Reward Location Information',
            {
                'fields': (
                    'location',
                    'reward',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Reward Location',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'location',
                    'reward',
                ),
            },
        ),
    )
    
    
# Reward Earning Admin Portal
class RewardEarningAdmin(admin.ModelAdmin):

    add_form = RewardEarningAddForm
    form = RewardEarningForm

    model = RewardEarning
    
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'user',
        'reward',
        'amount_earned',
    ]
    
    search_fields = [
        'reward',
    ]
    
    ordering = [
        'user',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                )
            },
        ),
        (
            'Reward Earning',
            {
                'fields': (
                    'user',
                    'reward',
                    'amount_earned',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Reward Earning',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'reward_program',
                    'user',
                    'granted_by_staff',
                    'reward',
                    'amount_earned',
                ),
            },
        ),
    )
    
    
# Reward Adjustment Admin Portal
class RewardAdjustmentAdmin(admin.ModelAdmin):

    add_form = RewardAdjustmentAddForm
    form = RewardAdjustmentForm

    model = RewardEarning
    
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'user',
        'adjustment_type',
        'reward',
        'adjustment_amount',
    ]
    
    search_fields = [
        'user',
    ]
    
    ordering = [
        'user',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                )
            },
        ),
        (
            'Reward Adjustment',
            {
                'fields': (
                    'user',
                    'adjustment_type',
                    'reason',
                    'reward',
                    'adjustment_amount',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Reward Adjustment',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'user',
                    'reward_program',
                    'location',
                    'adjustment_type',
                    'reward',
                    'adjustment_amount',
                ),
            },
        ),
    )
    
    
# Reward Redemption Admin Portal
class RewardRedemptionAdmin(admin.ModelAdmin):

    add_form = RewardRedemptionAddForm
    form = RewardRedemptionForm

    model = RewardRedemption
    
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'user',
        'reward',
        'amount_redeemed',
    ]
    
    search_fields = [
        'user',
    ]
    
    ordering = [
        'user',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                )
            },
        ),
        (
            'Reward Adjustment',
            {
                'fields': (
                    'user',
                    'reward',
                    'amount_redeemed',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Reward Adjustment',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'processed_by_staff',
                    'user',
                    'reward_program',
                    'location',
                    'reward',
                    'amount_redeemed',
                ),
            },
        ),
    )
    
    
admin.site.register(RewardProgramType, RewardProgramTypeAdmin)
admin.site.register(RewardProgram, RewardProgramAdmin)
admin.site.register(RewardProgramLocation, RewardProgramLocationAdmin)
admin.site.register(Reward, RewardAdmin)
admin.site.register(RewardLocation, RewardLocationAdmin)
admin.site.register(RewardEarning, RewardEarningAdmin)
admin.site.register(RewardAdjustment, RewardAdjustmentAdmin)
admin.site.register(RewardRedemption, RewardRedemptionAdmin)