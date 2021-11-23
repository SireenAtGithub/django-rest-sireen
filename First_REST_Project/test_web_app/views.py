from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework import status
from . models import Artist
from . serializers import ArtistSerializer


class ArtistList(APIView):
    def get(self, request):
        artist_name = Artist.objects.all()
        serializer = ArtistSerializer(artist_name, many=True)
        return Response(serializer.data)

    def post(self):
        pass