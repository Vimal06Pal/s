from rest_framework import serializers
from .models import Student

class Studentserializers(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        '''validate data --- we want to '''
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''this method takes 2 argument
        instance ===> old data in db that we want to replace
        validated_data ==> new data which we want to put in the db'''
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance