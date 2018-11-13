
#developer's defined URLs
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from  . import views

router=DefaultRouter()
router.register('movies-viewset', views.MoviesViewSet,base_name='movies-viewset')

urlpatterns=[
    path('movies/',views.MoviesApiView.as_view()),
    path('',include(router.urls)),
    path('users/',views.UserProfilesApiView.as_view()),

]