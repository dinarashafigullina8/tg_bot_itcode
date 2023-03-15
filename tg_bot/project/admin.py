from django.contrib import admin
from project.models import Request, User

class RequestsAdmin(admin.ModelAdmin):
    list_display = ('region',)
    

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id',)
   
admin.site.register(Request, RequestsAdmin)
admin.site.register(User, UserAdmin)


