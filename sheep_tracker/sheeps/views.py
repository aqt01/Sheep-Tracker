from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, filters
from sheeps.serializers import *    
from django.http import HttpResponseRedirect

from sheeps.models import Person

def url_redirect_home(request):
    return HttpResponseRedirect("/home/")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('-id')
    serializer_class = PersonSerializer