from django.db.models import fields
from .models import *
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','durations']

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id','name','gender']