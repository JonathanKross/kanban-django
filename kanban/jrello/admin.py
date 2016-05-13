from django.contrib import admin
from .models import Jrello


class JrelloAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_completed', 'priority', 'last_edited')


admin.site.register(Jrello, JrelloAdmin)
