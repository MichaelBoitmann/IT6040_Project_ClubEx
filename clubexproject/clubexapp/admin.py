from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Video, Category

from embed_video.admin import AdminVideoMixin

class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
        list_display = ('title', 'category',)
        search_fields = ('title', 'category',)

        filter_horizontal = ()
        list_filter = ()
        fieldsets = ()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, AdminVideo)
