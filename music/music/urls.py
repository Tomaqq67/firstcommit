from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path('genres', views.genres),
    path('tracks', views.tracks),
    path('delete/<int:id_genres>', views.delete),
    path('add_genre/', views.add_genre),
    path('editgenre/<int:id_genres>', views.edit_genre),
    
    path('artists/', views.artists),
    path('add_artist/', views.add_artist),

    path('add_track/', views.add_track),
    path('deletetrack/<int:id_track>', views.deletetrack),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
