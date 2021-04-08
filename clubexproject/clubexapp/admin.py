from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Program

class ProgramAdmin(admin.ModelAdmin):
        list_display = ('title','category',)
        search_fields = ('title','category',)

        filter_horizontal = ()
        list_filter = ()
        fieldsets = ()

admin.site.register(Program, ProgramAdmin)
