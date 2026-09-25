from django.shortcuts import render
from .models import Album

def music_list(request):
    albums = Album.objects.all()
    return render(request, 'music/music_list.html', {'albums': albums})