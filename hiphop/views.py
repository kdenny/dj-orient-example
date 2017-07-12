# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(request):
    artists = Artist.objects.all()

    artist = Artist.objects.filter(name = "Kanye West")[0]
    a = artist.out_artist_album[0]

    aalbs = artist_album.objects.filter(id=a)
    album_id = aalbs[0].in_vertex

    print(album_id)
    b = Album.objects.filter(id=album_id)
    print(b)






    output = ', '.join([a.name for a in artists])
    return HttpResponse(output)