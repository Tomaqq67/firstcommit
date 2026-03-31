from django.shortcuts import render, redirect 
from .models import Genre,Track, Artist
from django.http import HttpResponseRedirect, HttpResponse
from .forms import GenreForm, TrackForm, ArtistsForm



def index(request):
    return render(request, 'index.html')

def genres (request):
    genres = Genre.objects.all() 
    return render(request, 'genres.html', {'genres': genres, 'page': 'genres'})

def tracks(request):
    tracks = Track.objects.all()
    genres = Genre.objects.all()
    return render(request, 'tracks.html', {'tracks': tracks, 'genres': genres})

def delete(request, id_genres):
    genres = Genre.objects.get(id=id_genres)
    genres.delete()
    return HttpResponse('<h1>Успешно удалено</h1><br><a href="/">На главную</a>')

def add_genre(request):
    if request.method == 'POST':
        runame = request.POST.get("runame")
        name = request.POST.get("name")
        desc = request.POST.get("description")
        genre = Genre()
        genre.runame = runame
        genre.name = name
        genre.description = desc
        genre.save()
        return redirect('/genres')
    else:
        genreform = GenreForm()
        return render(request, "add_genre.html", {'form':genreform})

def edit_genre(request, id_genres):
    g = Genre.objects.get(id=id_genres)
    if request.method == "POST":
        genre = GenreForm(request.POST, instance=g)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    else:
        genreform=GenreForm(instance=g)
        return render(request,"add_genre.html", {'form': genreform})


def deletetrack(request, id_track):
    song = Track.objects.get(id=id_track)
    song.delete()
    return HttpResponse('<h1>Успешно удалено</h1><br><a href="/">На главную</a>')

def add_track(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        duration = request.POST.get("duration")
        genres = request.POST.get("genres")
        track = Track()
        track.name = name
        track.duration = duration
        track.genres = genres
        track.save()
        return redirect('/tracks')
    else:
        trackform = TrackForm()
        return render(request, "add_track.html", {'form':trackform})

def artists(request):
    a = Artist.objects.all()
    return render(request, 'artist.html', {'artists': a})