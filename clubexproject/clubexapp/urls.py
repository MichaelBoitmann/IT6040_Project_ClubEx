from django.urls import path

from .views import HomePageView, AboutPageView, CustomerPageView, video_index, search

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('search/', search, name='search'),
    path('', video_index),
]
