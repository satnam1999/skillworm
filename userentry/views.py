from django.shortcuts import render, redirect
from accounts import views
from homepage import views as hviews
from pyexpat.errors import messages


def login(request):
    if request.method == 'POST':
        key = views.login(request)
        if key == 3:
            return redirect('/')
        elif key == 4:
            return render(request, 'loginregister.html', {'key': 0, 'alert': 0})
    else:
        return render(request, 'loginregister.html', {'key': 0})


def logout(request):
    views.logout(request)
    return redirect('/')
    #return render(request, 'home.html', {'alert': 1})


def register(request):
    if request.method == 'POST':
        key = views.register(request)
        if key == 0:
            return redirect('/account/login')
            #return render(request, "loginregister.html", {'key': key, 'alert': 2})
        else:
            return render(request, "loginregister.html", {'key': key, 'alert': 3})
    else:
        return render(request, "loginregister.html", {'key': 1})
