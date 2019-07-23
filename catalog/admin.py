from django.contrib import admin
from catalog.models import Genre, Movie, Actor, Director

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Genre)
# admin.site.register(Movie)
admin.site.register(Actor)
# admin.site.register(Director)
# Register your models here.

admin.site.register(Director, DirectorAdmin)

@admin.register(Movie)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'display_genre', 'display_actor')
