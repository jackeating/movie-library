from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Director


from catalog.models import Genre, Actor, Movie, Director

def index(request):

    
    num_movies = Movie.objects.all().count()

    num_directors = Director.objects.count()
    num_actors = Actor.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_movies' : num_movies,
        'num_directors': num_directors,
        'num_actors': num_actors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 5

class MovieDetailView(generic.DetailView):
    model = Movie

class DirectorCreate(CreateView):
    model = Director
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}

class DirectorUpdate(UpdateView):
    model = Director
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class DirectorDelete(DeleteView):
    model = Director
    success_url = reverse_lazy('Director')

class DirectorListView(generic.ListView):
    model = Director
    paginate_by = 5

class DirectorDetailView(generic.DetailView):
    model = Director

class ActorListView(generic.ListView):
    model = Actor
    paginate_by = 5
