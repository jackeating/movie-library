from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('movies/', views.MovieListView.as_view(), name='movies'),
path('movie/<int:pk>', views.MovieDetailView.as_view(), name='movie-detail'),
path('director/create/', views.DirectorCreate.as_view(), name='director_create'),
path('director/<int:pk>/update/', views.DirectorUpdate.as_view(), name='director_update'),
path('director/<int:pk>/delete/', views.DirectorDelete.as_view(), name='director_delete'),
path('directors/', views.DirectorListView.as_view(), name='directors'),
path('director/<int:pk>', views.DirectorDetailView.as_view(), name='director-detail'),
path('actors', views.ActorListView.as_view(), name='actors'),


# path('movie/<uuid:pk>/renew/', views.renew_movie_librarian, name='renew-movie-librarian'),


]
