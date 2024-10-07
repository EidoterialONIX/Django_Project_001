from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):

    content = """
    
        <h1>Home</h1>
        <p>Constins</p>
    
    """

    return HttpResponse(content)
