from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("issue_tracking_system/", include("issue_tracking_system.urls")),
    path("admin/", admin.site.urls),

]