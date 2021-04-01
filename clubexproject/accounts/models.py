from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,username, email, first_name, last_name, password=None):
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have a valid email")
        if not first_name:
            raise ValueError("Users must have a first_name")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    ANNUALLY="12 Months"
    MONTHLY="1 Month"
    UNSUBSCRIBED = "No active subscription"
    SUBSCRIPTION_CHOICES = [
        (ANNUALLY, "12 Months: $100"),
        (MONTHLY, "1 Month: $10"),
        (UNSUBSCRIBED, "No active subscription")

    ]
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    subscription = models.CharField(
        max_length=50,
        choices = SUBSCRIPTION_CHOICES,
        default=UNSUBSCRIBED,
        )

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email', 'first_name', 'last_name',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(slef, app_label):
        return True
