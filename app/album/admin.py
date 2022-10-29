from django.contrib import admin

from album.models import Artist, Album, Track


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'artist', 'year',)
    list_filter = ('name', 'year',)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'album',)
    list_filter = ('name',)