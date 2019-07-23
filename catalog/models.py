from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
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

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='要約を入力してください')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='ジャンルを選択してください')
    actor = models.ManyToManyField(Actor, help_text='役者を選択してください')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this movie."""
        return reverse('movie-detail', args=[str(self.id)])

    def display_genre(self):
            """Create a string for the Genre. This is required to display genre in Admin."""
            return ', '.join(genre.name for genre in self.genre.all()[:3])

            display_genre.short_description = 'Genre'

    def display_actor(self):
            """Create a string for the Genre. This is required to display genre in Admin."""
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
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
