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
    
