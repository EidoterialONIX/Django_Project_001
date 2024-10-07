from django.urls import  path
import projects.adrian_project.home.views.py

urlpatterns = [
    path('', home, name="home" )
]