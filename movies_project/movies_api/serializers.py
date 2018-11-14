from rest_framework import serializers

from . import models

class MovieSerializer(serializers.ModelSerializer):
    """Serialize a title field for testing Movies APIView"""
    class Meta:
        model=models.Movie
        fields=('id', 'title', 'duration','year','director','writer')                

    def create(self,validated_data):
    
        movie=models.Movie(
            title=validated_data['title'],
            duration=(validated_data['duration']*60), #in minutes but the default form is in seconds
            year=validated_data['year'],
            director=validated_data['director'],
            writer=validated_data['writer'],            
        )       
        
        movie.save()
        return movie


    # title=serializers.CharField(max_length=255)
    # duration_minute=serializers.IntegerField()
    # year=serializers.IntegerField()
    # director=serializers.CharField(max_length=50)
    # writer=serializers.CharField(max_length=50)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize a name field for testing UserProfiles APIView"""
    class Meta:
        model=models.UserProfile
        fields=('id', 'email', 'name','password')
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validated_data):

        user=models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

        # name=serializers.CharField(max_length=100)
        # email=serializers.EmailField(max_length=100)
        # password=serializers.CharField(max_length=100,min_length=8,style={'input_type':'password'})
        # password_confirmation=serializers.CharField(max_length=100,min_length=8,style={'input_type':'password','placeholder':"re-enter your password to confirm"})