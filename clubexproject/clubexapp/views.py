from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Video


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class CustomerPageView(TemplateView):
    template_name = 'customer.html'


def video_index(request):
    videos = Video.objects.all()
    return render(request, 'videos_folder/video_tube.html', context={'videos': videos})
