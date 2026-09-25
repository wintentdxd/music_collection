"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from music import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  #шляхи входу/виходу
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),  #Реєстрація
    
    path('', views.AlbumListView.as_view(), name='album_list'),
    path('top-albums/', views.TopAlbumsView.as_view(), name='top_albums'),
    path('albums/my/', views.MyAlbumsView.as_view(), name='my_albums'),  # Мої альбоми 
    path('albums/new/', views.AlbumCreateView.as_view(), name='album_create'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('albums/<int:pk>/edit/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('albums/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
    path('artists/', views.ArtistListView.as_view(), name='artist_list'),
]