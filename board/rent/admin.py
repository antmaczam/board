from django.contrib import admin
from rent.models import Game
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status',)
    list_filter = ('name', 'price', 'status',)

    search_fields = ('name',) 

    actions = []

admin.site.register(Game,GameAdmin)