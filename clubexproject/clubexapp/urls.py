from django.urls import path

from .views import views, HomePageView, AboutPageView, ProgramsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('programs/', ProgramPageView.as_view(), name='programs'),
]
