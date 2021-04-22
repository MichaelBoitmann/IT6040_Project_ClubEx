from django.urls import path

<<<<<<< HEAD
from .views import HomePageView, AboutPageView, CustomerPageView, video_index

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('video/', video_index, name='video'),
=======
from .views import HomePageView, AboutPageView, CustomerPageView, video_index, search

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('search/', search, name='search'),
    path('', video_index),
>>>>>>> origin/edit-1
]
