from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def blog_home(request):
    # return HttpResponse("Welcome to the Blog Home Page!")
    template = loader.get_template('first-blog.html')
    return HttpResponse(template.render({}, request))