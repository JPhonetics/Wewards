from django import forms
from apps.rewards.models import (
    RewardProgramType,
    RewardProgram,
    RewardProgramLocation,
    Reward,
    RewardLocation,
    RewardEarning,
    RewardAdjustment,
    RewardRedemption,
)

## Reward Program Type Forms
class RewardProgramTypeAddForm(forms.ModelForm):
    
    class Meta:
        model = RewardProgramType
        fields = '__all__'


class RewardProgramTypeForm(forms.ModelForm):
    
    class Meta:
        model = RewardProgramType
        fields = '__all__'
        

## Reward Program Forms       
class RewardProgramAddForm(forms.ModelForm):
    
    class Meta:
        model = RewardProgram
        fields = '__all__'


class RewardProgramForm(forms.ModelForm):
    
    class Meta:
        model = RewardProgram
        fields = '__all__'
        
        
## Reward Program Location Forms
class RewardProgramLocationAddForm(forms.ModelForm):
    
    class Meta:
        model = RewardProgramLocation
        fields = '__all__'


class RewardProgramLocationForm(forms.ModelForm):
    
    class Meta:
        model = RewardProgramLocation
        fields = '__all__'
        

## Reward Forms        
class RewardAddForm(forms.ModelForm):
    
    class Meta:
        model = Reward
        fields = '__all__'


class RewardForm(forms.ModelForm):
    
    class Meta:
        model = Reward
        fields = '__all__'
        
        
## RewardLocation Forms        
class RewardLocationAddForm(forms.ModelForm):
    
    class Meta:
        model = RewardLocation
        fields = '__all__'


class RewardLocationForm(forms.ModelForm):
    
    class Meta:
        model = RewardLocation
        fields = '__all__'
        

## Reward Earning Forms        
class RewardEarningAddForm(forms.ModelForm):
    
    class Meta:
        model = RewardEarning
        fields = '__all__'


class RewardEarningForm(forms.ModelForm):
    
    class Meta:
        model = RewardEarning
        fields = '__all__'
        
        
## Reward Adjustment Forms        
class RewardAdjustmentAddForm(forms.ModelForm):
    
    class Meta:
        model = RewardAdjustment
        fields = '__all__'


class RewardAdjustmentForm(forms.ModelForm):
    
    class Meta:
        model = RewardAdjustment
        fields = '__all__'
        
        
## Reward Redemption Forms        
class RewardRedemptionAddForm(forms.ModelForm):
    
    class Meta:
        model = RewardRedemption
        fields = '__all__'


class RewardRedemptionForm(forms.ModelForm):
    
    class Meta:
        model = RewardRedemption
        fields = '__all__'