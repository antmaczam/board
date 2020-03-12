from django.contrib import admin
from rent.models import Game, Rent
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status',)
    list_filter = ('name', 'price', 'status',)

    search_fields = ('name',) 

    actions = []

class RentAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'user', 'status',)
    list_filter = ('ticker', 'user', 'status',)

    search_fields = ('ticker', 'user', 'status',) 

    actions = []

admin.site.register(Game,GameAdmin)
admin.site.register(Rent,RentAdmin)