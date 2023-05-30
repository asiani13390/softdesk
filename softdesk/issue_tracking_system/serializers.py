from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User 

from .models import Project
from .models import Contributor

class SignupSerializer(ModelSerializer):

    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'username','email', 'password','date_joined')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        return User.objects.create_user(**data)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

