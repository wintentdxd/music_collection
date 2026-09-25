from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Album, Artist, Genre


# View для реєстрації
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


# Список усіх альбомів
class AlbumListView(ListView):
    model = Album
    template_name = 'music/album_list.html'
    context_object_name = 'albums'
    paginate_by = 5


# Топ альбоми
class TopAlbumsView(ListView):
    model = Album
    template_name = 'music/album_list.html'
    context_object_name = 'albums'
    paginate_by = 5

    def get_queryset(self):
        return Album.objects.filter(rating=5)


# Деталі альбому
class AlbumDetailView(DetailView):
    model = Album
    template_name = 'music/album_detail.html'
    context_object_name = 'album'


# Створити альбом (автоматично проставляємо owner)
class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'artist', 'genres', 'album_type', 'release_date', 'rating']
    template_name = 'music/album_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# Редагувати альбом (тільки власник або staff)
class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['title', 'artist', 'genres', 'album_type', 'release_date', 'rating']
    template_name = 'music/album_form.html'

    def test_func(self):
        album = self.get_object()
        return album.owner == self.request.user or self.request.user.is_staff


# Видалити альбом (тільки власник або staff)
class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'music/album_confirm_delete.html'
    success_url = reverse_lazy('album_list')

    def test_func(self):
        album = self.get_object()
        return album.owner == self.request.user or self.request.user.is_staff


# Мої альбоми
class MyAlbumsView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'music/album_list.html'
    context_object_name = 'albums'
    paginate_by = 5

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)


# Список виконавців
class ArtistListView(ListView):
    model = Artist
    template_name = 'music/artist_list.html'
    context_object_name = 'artists'