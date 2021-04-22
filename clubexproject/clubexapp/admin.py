from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Video, Category

from embed_video.admin import AdminVideoMixin

<<<<<<< HEAD
=======

>>>>>>> origin/edit-1
class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
<<<<<<< HEAD
        list_display = ('title', 'category',)
        search_fields = ('title', 'category',)

        filter_horizontal = ()
        list_filter = ()
        fieldsets = ()
=======
    list_display = ('id', 'category', 'title')
    search_fields = ('category', 'title',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

>>>>>>> origin/edit-1

admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, AdminVideo)
