from django.contrib import admin
from .models import Genre, Artist, Album, Track

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('name', 'country')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album_type', 'release_date', 'rating')
    list_filter = ('album_type', 'genres', 'release_date')
    search_fields = ('title', 'artist__name')
    filter_horizontal = ('genres',)
    actions = ['set_rating_5']

    @admin.action(description='Встановити рейтинг 5 для обраних')
    def set_rating_5(self, request, queryset):
        updated = queryset.update(rating=5)
        self.message_user(request, f'Оновлено {updated} альбомів.')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'duration_formatted')
    search_fields = ('title', 'album__title')