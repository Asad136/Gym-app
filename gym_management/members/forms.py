from django import forms
from .models import Member,FeePayment

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone_number', 'fee_amount', 'fee_date', 'picture', 'status']
class FeePaymentForm(forms.ModelForm):
    class Meta:
        model = FeePayment
        fields = ['amount', 'date']