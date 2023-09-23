from django.contrib import admin
from .models import Movie, Tag, Category
from django.utils.html import format_html

# Register your models here.
class MovieAdmin(admin.ModelAdmin):

    def preview(self, movie):
        return format_html(
            f'<img style="height: 200px" src="/media/{movie.preview_image}" />'
        )
    
    def movie(self, movie):
          
        return format_html(
            f"""
                <video width="320" height="240" controls>
                    <source src="/media/{movie.file}" type="video/mp4">
                    <your browser doesn't sup[port the video tag>
                </video>"""
        )
        



    preview.short_description = 'Movie image'
    movie.short_description = 'movie video'
    list_display = ['name', 'preview', 'movie', 'description']

    

admin.site.register(Movie, MovieAdmin)
admin.site.register(Tag)
admin.site.register(Category)
