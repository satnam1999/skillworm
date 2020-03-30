from django.shortcuts import render
from .models import Skill
import random
from django.contrib.auth.decorators import login_required


def home(request):
    n = Skill.objects.count()
    r = []
    while len(r) < 4:
        rt = random.randrange(1, n + 1, 1)
        if rt not in r:
            r += [rt]
    print(r)
    skill_grp = Skill.objects.filter(id__in=r)
    print(skill_grp)

    return render(request, 'home.html', {'skills': skill_grp})


def search(request): 
    s =''      
    if request.method == 'GET': # this will be GET now      
        s =  request.GET.get('search').lower() # do some research what it does
        print(s)       
    skill_grp = Skill.objects.filter(skill_url__contains=s)
    print(skill_grp)
    
    return render(request, 'home.html',{'skills':skill_grp}) 


def chat(request): 
    return render(request, 'index.html') 

#cust_name = request.user.first_name
@login_required
def profile(request):  
    pass

