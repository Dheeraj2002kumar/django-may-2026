from django import template
from django.template import loader
from django.http import HttpResponse
from .models import Member

# Create your views here.
def member_list(request):
    # return HttpResponse("This is the member list view.")
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())

    template = loader.get_template('all_members.html')
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry']
    }
    return HttpResponse(template.render(context, request))