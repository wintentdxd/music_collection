from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Album, Artist

# ЧАСТИНА 1: CBV ДЛЯ ПЕРЕГЛЯДУ

# 1. Список альбомів з пагінацією
class AlbumListView(ListView):
    model = Album
    template_name = 'music/album_list.html'
    context_object_name = 'albums'
    ordering = ['title']
    paginate_by = 5


# 2. Другий список із фільтрацією
class TopAlbumsView(ListView):
    model = Album
    template_name = 'music/album_list.html'
    context_object_name = 'albums'
    paginate_by = 5

    def get_queryset(self):
        return Album.objects.filter(rating__gte=4).order_by('-rating')


# 3. Деталі альбому з додатковим контекстом
class AlbumDetailView(DetailView):
    model = Album
    template_name = 'music/album_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_albums'] = Album.objects.filter(
            artist=self.object.artist
        ).exclude(pk=self.object.pk)
        return context


# 4. Список виконавців
class ArtistListView(ListView):
    model = Artist
    template_name = 'music/artist_list.html'
    context_object_name = 'artists'


# ЧАСТИНА 2: CRUD ОПЕРАЦІЇ
class AlbumCreateView(CreateView):
    model = Album
    fields = ['title', 'artist', 'genres', 'album_type', 'release_date', 'rating']
    template_name = 'music/album_form.html'


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['title', 'artist', 'genres', 'album_type', 'release_date', 'rating']
    template_name = 'music/album_form.html'


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'music/album_confirm_delete.html'
    success_url = reverse_lazy('album_list')


# def album_list(request):
#     ...
# def album_detail(request, pk):
#     ...
# def artist_list(request):
#     ...