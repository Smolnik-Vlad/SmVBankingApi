from django.contrib import admin

from users.models import UserProfile, Client


# Register your models here.
class CommonUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'password')
    empty_value_display = "undefined"



class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'work_place')
    list_editable = ('work_place',)
    empty_value_display = "undefined"



admin.site.register(UserProfile, CommonUserAdmin)
admin.site.register(Client, ClientAdmin)
