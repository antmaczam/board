from django.contrib import admin

# Register your models here.
from reviews.models import Valoration, Comment


class ValorationAdmin(admin.ModelAdmin):
    list_display = ('toUser', 'rate',)
    list_filter = ('toUser', 'rate',)

    search_fields = ('toUser', 'rate',)

    actions = []


class CommentAdmin(admin.ModelAdmin):
    list_display = ('toUser', 'comment',)
    list_filter = ('toUser', 'comment',)

    search_fields = ('toUser', 'comment',)

    actions = []


admin.site.register(Valoration, ValorationAdmin)
admin.site.register(Comment, CommentAdmin)
