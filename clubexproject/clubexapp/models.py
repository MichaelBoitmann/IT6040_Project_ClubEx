from django.db import models

class Customer(models.Model):
    SUBSCRIPTION_TYPE = [
    ('1 Year: $100',"Annually"),
    ('1 Month: $10','Monthly'),

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subscription = models.CharField(max_length=1, choices=SUBSCRIPTION_TYPE)
