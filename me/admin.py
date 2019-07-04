from django.contrib import admin

from .models import perfil

@admin.register(perfil)
class perfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profesion')
