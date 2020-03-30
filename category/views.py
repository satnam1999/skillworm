from django.shortcuts import render
from homepage.models import Category, Skill


# Create your views here.

def category(request):
    skill_list = Skill.objects.all()
    category_list = Category.objects.all()
    params = {'categories': category_list}
    return render(request, 'categorypage.html', params)


def show(request, skill_selected):
    return render(request, 'searchresult.html')