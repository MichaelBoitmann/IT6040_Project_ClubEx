from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Video

from embed_video.admin import AdminVideoMixin

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
        list_display = ('title', 'category',)
        search_fields = ('title', 'category',)

        filter_horizontal = ()
        list_filter = ()
        fieldsets = ()


admin.site.register(Video, AdminVideo)
