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
    # mydata = Member.objects.all().values()
    # mydata = Member.objects.values_list('firstname')
    mydata = Member.objects.filter(firstname='Dheeraj').values()
    # mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
        # 'mymembers': mymembers,
        'x': ['Apple', 'Banana', 'Cherry'],
        'y': ['Apply', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))