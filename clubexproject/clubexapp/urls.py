from django.urls import path

from .views import HomePageView, AboutPageView, CustomerPageView, video_index

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('video/', video_index, name='video'),
]
