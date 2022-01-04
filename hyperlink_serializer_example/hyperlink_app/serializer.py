from django.db.models import fields
from .models import *
from rest_framework import serializers


class SnippetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ['id','created','title','language']


class SnippetsDetailSerializer(serializers.ModelSerializer):
    print("cvchvhvx++++++++++++")
    snippet_details = serializers.HyperlinkedIdentityField(view_name='snip:snippet-detail', many=True, read_only=True)
    class Meta:
        model = Snippets
        # fields = ['title']
        fields = ('snippet_details','title')

