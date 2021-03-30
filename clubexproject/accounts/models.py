from django.db import models

class Subscription(models.Model):
    ANNUALLY="12 Months"
    MONTHLY="1 Month"
    SUBSCRIPTION_CHOICES = [
        (ANNUALLY, "12 Months: $100"),
        (MONTHLY, "1 Month: $10"),
    ]
    subscription_type = models.CharField(
        max_length=15,
        choices = SUBSCRIPTION_CHOICES,
        default=ANNUALLY,
        )

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    subscription_type = models.ForeignKey(Subscription, on_delete=models.CASCADE, default=None, blank=True, null=True)
