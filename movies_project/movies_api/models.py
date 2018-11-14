from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class MovieManager():
    
    def create_movie(self,title,duration,year,director,writer):
        
        if not title:
             raise ValueError('Movie must have a title')
        
        email=self.normalize_email(email) #to normalize upper or lower case
        movie=self.model(title=title,duration=duration,year=year,director=director,writer=writer)
        
        movie.save(using=self.db)

        return movie

class Movie(models.Model):
    """Represents a movie"""""
    
    title=models.CharField(max_length=255, unique=True)
    duration=models.DurationField("Duration (minutes)")    
    year=models.IntegerField()
    director=models.CharField(max_length=255)
    writer=models.CharField(max_length=255)

    REQUIRED_FIELDS=['title']

    objects=MovieManager()
    
    def __str__(self):
        return self.title


class UserProfileManager(BaseUserManager):
    
    def create_user(self,email,name,password=None):
        
        if not email:
             raise ValueError('Users must have an email address')
        
        email=self.normalize_email(email) #to normalize upper or lower case
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self,email,name,password):
        
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return self


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_name(self):
        
        return self.name
    
    def __str__(self):
        return self.email
    
