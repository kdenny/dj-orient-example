# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from Djangorient.DjangorientModels import *
from django_orientdb.models import *

from django.db import models

# Create your models here.

class Artist(DjangorientNode):
	name = String()
	popularity = Integer()
	uri = String()

class Album(DjangorientNode):
	title = String()
	uri = String()

class Track(DjangorientNode):
	name = String()
	popularity = Integer()
	uri = String()
	track_num = Integer()


class artist_album(DjangorientEdge):
	name = String()
	uri = String()