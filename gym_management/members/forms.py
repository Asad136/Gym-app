from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone_number', 'fee_amount', 'fee_date', 'picture', 'status']
