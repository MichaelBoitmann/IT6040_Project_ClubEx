from django.db import models

class Subscription(models.Model):
    subscription_type = models.CharField(max_length=30)

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, default=None, blank=True, null=True)
