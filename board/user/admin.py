from django.contrib import admin
from user.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','name', 'lastName', 'range', 'rate',)
    list_filter = ('username','name', 'lastName', 'range', 'rate',)

    search_fields = ('username','name', 'lastName', 'rabge', 'rate',) 

    actions = []

admin.site.register(User,UserAdmin)