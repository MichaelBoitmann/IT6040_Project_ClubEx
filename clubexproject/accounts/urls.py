from django.urls import path

from accounts.views import(registration_view,)

urlpatterns = [
    path('signup/', registration_view, name='signup'),
]
