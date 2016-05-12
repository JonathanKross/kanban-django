from django.contrib import admin
from .models import Jrello


class JrelloAdmin(admin.JrelloAdmin):
    list_display = ['title', 'is_completed', 'priority']


admin.site.register(Jrello, JrelloAdmin)
