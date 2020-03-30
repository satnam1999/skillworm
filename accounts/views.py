from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from userentry import views
from .models import UserType


# Create your views here.

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(username=email, password=password)

    if user is not None:
        auth.login(request, user)
        return 3
    else:
        return 4


def logout(request):
    auth.logout(request)


def register(request):
    first_name = ''
    last_name = ''
    if request.method == 'POST':
        name = request.POST['name']
        if not name.isalpha:
            if ' ' in name:
                name = name.split()
                first_name = name[0]
                last_name = name[1]
        else:
            first_name = name
        username = request.POST['email']
        password = request.POST['password']
        email = request.POST['email']
        type_user = request.POST['type']

        if password == password:
            if User.objects.filter(username=email).exists():
                print('Username taken')
                return 1
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                if type_user == 'Student':
                    v1 = UserType(user=user, student=True)
                    v1.save()
                    print('Student')
                elif type_user == 'Teacher':
                    v1 = UserType(user=user, teacher=True)
                    v1.save()
                    print('Teacher')
                print('user created')
                return 0
