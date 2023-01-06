from django.contrib import admin
from .models import Book, Genre, BookAuthorsFoto, Authors

admin.site.register(BookAuthorsFoto)
class BookAuthorsFotoInline(admin.TabularInline):
    model = BookAuthorsFoto
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = 'russian_name','cover_img','price','make_year'
    inlines = BookAuthorsFotoInline,
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = 'name',


admin.site.register(Authors)