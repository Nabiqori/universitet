from django.contrib import admin

from .models import *
class UstozAdmin(admin.ModelAdmin):
    list_display = ["nom"]
    search_fields = ['nom']
class YonalishAdmin(admin.ModelAdmin):
    list_display = ["nom", "aktiv"]
    list_filter = ["nom", "aktiv"]
class FanAdmin(admin.ModelAdmin):
    list_display = ["nom", 'yonalish', 'asosiy']
    list_filter = ["yonalish","asosiy"]
    search_fields = ["yonalish","asosiy"]
admin.site.register(Ustoz,UstozAdmin)
admin.site.register(Yonalish,YonalishAdmin)
admin.site.register(Fan,FanAdmin)
