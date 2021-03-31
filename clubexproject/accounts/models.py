from django.db import models
from django.forms import ModelForm

class Customer(models.Model):
    ANNUALLY="12 Months"
    MONTHLY="1 Month"
    SUBSCRIPTION_CHOICES = [
        (ANNUALLY, "12 Months: $100"),
        (MONTHLY, "1 Month: $10"),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subscription = models.CharField(
        max_length=15,
        choices = SUBSCRIPTION_CHOICES,
        default=ANNUALLY,
        )
