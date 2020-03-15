from django.contrib import admin
from rent.models import Game, Rent
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status',)
    list_filter = ('name', 'price', 'status',)

    search_fields = ('name',) 

    actions = []

class RentAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'user', 'rentable',)
    list_filter = ('ticker', 'user', 'rentable',)

    search_fields = ('ticker', 'user', 'rentable',) 

    actions = []

admin.site.register(Game,GameAdmin)
admin.site.register(Rent,RentAdmin)