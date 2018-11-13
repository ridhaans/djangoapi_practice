from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
#developer's defined logic for the api
class MoviesApiView(APIView):

    serializer_class=serializers.MoviesSerializer

    def get(self, request, format=None):

        an_apiview=[
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Similar to Django pre-defined view',
            'Gives control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Movies!', 'an_apiview':an_apiview})

    def post(self,request):
        """Tells the duration of the film"""

        serializer = serializers.MoviesSerializer(data=request.data)

        if serializer.is_valid():
            title=serializer.data.get('title')
            year=serializer.data.get('year')
            duration=int(serializer.data.get('duration_minute'))
            message=f'Information about {title}({year}) movie is successfully added to the database'
            
            return Response({'message':message})        
        else:
            return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request,pK=None):
        
        serializer = serializers.MoviesSerializer(data=request.data)
        if serializer.is_valid():
            title=serializer.data.get('title')
            year=serializer.data.get('year')
        
            return Response({'message':f'Information about {title}({year}) is succesfully updated(put)'})
    
    def patch(self,request,pK=None):
        
        serializer = serializers.MoviesSerializer(data=request.data)
        if serializer.is_valid():
            title=serializer.data.get('title')
            year=serializer.data.get('year')
            return Response({'message':f'Information about {title}({year}) is succesfully updated(patch)'})
    
    def delete(self,request,pK=None):
        serializer = serializers.MoviesSerializer(data=request.data)
        if serializer.is_valid():
            title=serializer.data.get('title')
            year=serializer.data.get('year')
            return Response({'message':f'Information about {title}({year}) is succesfully deleted'})
    


class UserProfilesApiView(APIView):
    
    serializer_class=serializers.UserProfilesSerializer

    def get(self, request, format=None):

        an_apiview=[
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Similar to Django pre-defined view',
            'Gives control over your logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'User Profiles!', 'an_apiview':an_apiview})
    
    def post(self,request):
        """Say hello to the user"""

        serializer = serializers.UserProfilesSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})        
        else:
            return Response(
                serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )