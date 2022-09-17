from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.


def home(request):
    context={'home':'active'}
    return render (request, 'index.html', context)

def service(request):
    context={'service':'active'}
    return render (request, 'services.html', context)

def skill(request):
    context={'skill':'active'}
    return render (request, 'skill.html', context)

def projects(request):
    context={'projects':'active'}
    return render (request, 'projects.html', context)

def qualification(request):
    context={'qualification':'active'}
    return render (request, 'qualification.html', context)