from django.contrib import admin
from books.models import Author,Genre,Books
class BookAdmin(admin.ModelAdmin):
    list_display = ['name','author','genre','image','file','size','date']
    list_filter = ['author','genre','date']
    search_fields = ['name','author','genre']
    prepopulated_fields = {'slug':['name',]}
    date_hierarchy = 'date'
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name',]}
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name',]}
admin.site.register(Books,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre,GenreAdmin)

# Register your models here.
