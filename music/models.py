from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name="Жанр")

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Виконавець")
    country = models.CharField(max_length=50, blank=True, verbose_name="Країна")

    def __str__(self):
        return self.name


class Album(models.Model):
    TYPE_CHOICES = [
        ('lp', 'Повноформатний альбом (LP)'),
        ('ep', 'Міні-альбом (EP)'),
        ('single', 'Сінгл'),
        
    ]
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='albums', 
        null=True, 
        blank=True,
    )
    title = models.CharField(max_length=150, verbose_name="Назва альбому")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', verbose_name="Виконавець")
    genres = models.ManyToManyField(Genre, blank=True, related_name='albums', verbose_name="Жанри")
    album_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='lp', verbose_name="Тип")
    release_date = models.DateField(verbose_name="Дата релізу")
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оцінка (1-5)"
    )
    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return f"{self.artist.name} – {self.title}"

    def get_absolute_url(self):
        return reverse('album_detail', kwargs={'pk': self.pk})


class Track(models.Model):
    title = models.CharField(max_length=150, verbose_name="Назва треку")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks', verbose_name="Альбом")
    duration_seconds = models.PositiveIntegerField(verbose_name="Тривалість (сек)")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.album.title} - {self.title}"

    @property
    def duration_formatted(self):
        """Обчислюване поле: переводить секунди у формат ХХ:ХХ"""
        minutes = self.duration_seconds // 60
        seconds = self.duration_seconds % 60
        return f"{minutes}:{seconds:02d}"