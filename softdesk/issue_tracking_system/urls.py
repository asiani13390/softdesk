from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import SignupAPIView
from .views import ProjectsViewset
from .views import ProjectsUsersViewset

#from .views import ProjectRetrieveUpdateDestroyView
#from .views import ProjectListCreateAPIView


router = routers.DefaultRouter()
router.register(r'projects', ProjectsViewset, basename='projects')
router.register(r'projects/(?P<project_id>[0-9]+)/users', ProjectsUsersViewset, basename='projects-users')

urlpatterns = [

    # JWT Users
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # Import router urls
    path("", include(router.urls)),


]