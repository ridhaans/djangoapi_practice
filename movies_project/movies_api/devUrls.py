
#developer's defined URLs
from django.urls import path
from  . import views

urlpatterns=[
    path('movies/',views.MoviesApiView.as_view()),
    path('users/',views.UserProfilesApiView.as_view()),
]