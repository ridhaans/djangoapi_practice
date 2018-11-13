from rest_framework import serializers

class MoviesSerializer(serializers.Serializer):
    """Serialize a title field for testing Movies APIView"""
    
    title=serializers.CharField(max_length=255)
    duration_minute=serializers.IntegerField()
    year=serializers.IntegerField()
    director=serializers.CharField(max_length=50)
    writer=serializers.CharField(max_length=50)


class UserProfilesSerializer(serializers.Serializer):
    """Serialize a name field for testing UserProfiles APIView"""
    
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    password=serializers.CharField(max_length=100,min_length=8,style={'input type':'password'})
    password_confirmation=serializers.CharField(max_length=100,min_length=8,style={'input type':'password','placeholder':"re-enter your password to confirm"})
    
    
