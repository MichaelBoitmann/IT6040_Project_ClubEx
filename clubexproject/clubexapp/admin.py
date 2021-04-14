from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Program, Video

from embed_video.admin import AdminVideoMixin


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    search_fields = ('title', 'category',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Program, ProgramAdmin)


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, AdminVideo)
