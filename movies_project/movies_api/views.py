from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
#developer's defined logic for the api
class MoviesApiView(APIView):

    def get(self, request, format=None):

        an_apiview=[
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Similar to Django pre-defined view',
            'Gives control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Movies!', 'an_apiview':an_apiview})

class UserProfilesApiView(APIView):
    
    def get(self, request, format=None):

        an_apiview=[
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Similar to Django pre-defined view',
            'Gives control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'User Profiles!', 'an_apiview':an_apiview})
