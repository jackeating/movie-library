from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='映画のジャンルを入力してください')

    def __str__(self):
        return self.name



class Actor(models.Model):
    name = models.CharField(max_length=200, help_text='役者の名前を入力してください')

    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=200)

    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='要約を入力してください')

    genre = models.ManyToManyField(Genre, help_text='ジャンルを選択してください')
    actor = models.ManyToManyField(Actor, help_text='役者を選択してください')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])

    def display_genre(self):
            return ', '.join(genre.name for genre in self.genre.all()[:3])

            display_genre.short_description = 'Genre'

    def display_actor(self):
            return ', '.join(actor.name for actor in self.actor.all()[:3])

            display_actor.short_description = 'Actor'

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
