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

#@login_required
# #def category(request, pk):
#     ca_exercise = Exercise.objects.filter(category=pk).order_by('exercise_name')
#     categories = Category.objects.all().order_by('category_name')
#     return render(request, 'categories.html', {'pk':pk,'ca_exercise':ca_exercise, 'categories':categories})
#
# #@login_required
# def video(request):
#     category_exercise = video.objects.all().order_by('-views')
#     featured = category_exercise[0]
#     categories = Category.objects.all().order_by('category_name')
#     return render(request, 'exercise.html', {'category_exercise':category_exercise, 'categories':categories, 'featured':featured})
