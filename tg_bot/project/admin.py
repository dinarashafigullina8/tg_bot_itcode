from django.contrib import admin
from project.models import Request

class RequestsAdmin(admin.ModelAdmin):
    list_display = ('region',)
    
    
admin.site.register(Request, RequestsAdmin)
