from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from .views import SignupAPIView
from .views import ProjectListCreateAPIView

urlpatterns = [

    # JWT Users
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),


    # Project
    path('projects/', ProjectListCreateAPIView.as_view(), name='projects'),
]