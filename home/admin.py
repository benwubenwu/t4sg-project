from django.contrib import admin
from .models import NewUser
# Register your models here.
class NewUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'password', 'bio']

admin.site.register(NewUser, NewUserAdmin)