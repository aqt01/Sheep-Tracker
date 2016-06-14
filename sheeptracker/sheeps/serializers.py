from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sheeps.models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ( 'name', 'last_name', 'e-mail','telephone','cellphone')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

