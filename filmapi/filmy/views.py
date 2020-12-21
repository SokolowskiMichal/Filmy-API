from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import FilmSerializer, FilmFullSerializer
from .models import Film
from rest_framework.response import Response



class FilmViewset(viewsets.ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

    def retrieve(self, request, *args, **kwargs):
        film = self.get_object()
        serializer = FilmFullSerializer(film)
        return Response(serializer.data)
