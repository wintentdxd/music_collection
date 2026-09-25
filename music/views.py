from django.shortcuts import render, get_object_or_404
from .models import Album, Artist

# 1. Список альбомів (Головна сторінка)
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})

# 2. Сторінка деталей альбому (з get_object_or_404)
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})

# 3. Друга сторінка-список (Виконавці)
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})