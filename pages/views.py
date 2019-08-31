from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from swaraj_builder.models import Project, Quest, Record
from swaraj_builder.forms import QuestForm
from django.urls import reverse


# Create your views here.
def index(request):

    projects = Project.objects.all()
    records = Record.objects.all()
    context = {
        'projects' : projects,
        'records' : records
    }
    return render(request, 'index.html',context=context)


def about(request):
    records = Record.objects.all()
    context = {
        'records': records,
    }
    return render(request, 'about-us.html',context=context)


def service(request):
    return render(request, 'service.html')


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html',context=context)


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    quests = Quest.objects.all()
    context = {
       'quests': quests
    }

    return render(request, 'contact.html',context=context)


def questview(request):
    if request.method == 'POST':
        form = QuestForm(request.POST)
        # if form.is_valid():
        first_name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        quest_obj = Quest(first_name=first_name,phone=phone,subject=subject,message=message)  #get the data into quest model
        quest_obj.save()

        return HttpResponseRedirect(reverse(contact))
    else:
        form = QuestForm()

    return render(request,'contact.html',
                  {
                      'form' : form,
                  })