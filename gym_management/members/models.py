from django.db import models
from django.utils import timezone
from datetime import timedelta

class Member(models.Model):
    STATUS_CHOICES = (
        ('paid', 'paid'),
        ('Not paid', 'Not paid'),
    )

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee_date = models.DateField()
    picture = models.ImageField(upload_to='member_pictures/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.name
# for time calculate of month
    def fee_due_date(self):
        return self.fee_date + timedelta(days=30)
# for fee due date calculation
    def is_fee_due(self):
        return timezone.now().date() >= self.fee_due_date() - timedelta(days=2)
