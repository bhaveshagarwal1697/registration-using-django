from django.shortcuts import render
from django.http import *
from rest_framework import viewsets
from .models import Profile
from .serializers import UserSerializer


def home(request):
	return HttpResponse("<h1>Welcome To The Board<h1>")


class user_registration(viewsets.ModelViewSet):
 	queryset = Profile.objects.all()
 	serializer_class = UserSerializer