from django.shortcuts import render

# Create your views here.


# import forms
from basic_app.forms import UserForms,UserProfileForm

# importing required packages for Login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def special(request):
    return HttpResponse("you are logged in,nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def index(request):
    return render(request,'basic_app/index.html')

def basic(request):
    return render(request,'basic_app/base.html')

def registeration(request):
    registered=False

    if request.method=='POST':
        user_form=UserForms(request.POST)
        portfolio_form=UserProfileForm(request.POST)

        if user_form.is_valid() and  portfolio_form.is_valid():
            # print('this in console')
            # print('username:'+forms.cleaned_data['username'])
            # print('email:'+forms.cleaned_data['email'])
            # print('password:'+forms.cleaned_data['password'])
            # print('portfolio_link:'+forms.cleaned_data['portfolio_link'])
            #
            user=user_form.save()

            user.set_password(user.password)
            # this is hashing of password

            user.save()
            # this is final saving of data in database

            portfolio=portfolio_form.save(commit=False)
            # commit is equal to false due to not letting happen collision
            # this portfolio tries to overwrite previous define user

            # so we do
            portfolio.user=user
            # this set up one to one relationship we have already defined in models
            # between user in UserProfileInfo and User (built in model)

            # FOR DIFFERENT TYPES OF FILE LIKE PDF, CSV ,IMAGES WE USE
            # REQUEST.FILES
            if 'portfolio_image' in request.FILES:
                portfolio.portfolio_image=request.FILES['portfolio_image']
                # what name has given in model we use that

                portfolio.save()
            registered=True


        else:
            print(user_form.errors,portfolio_form.errors)
    else:
        user_form=UserForms()
        portfolio_form=UserProfileForm()


    return render(request,'basic_app/registration.html',{'user_form':user_form,'portfolio_form':portfolio_form,'registered':registered})


def user_login(request):

    if request.method=='POST':
        # if the user has filled the login form
        username=request.POST.get("username")
        # get the username same name inside get as written in input tag
        password=request.POST.get('password')

        # authenticationg the user ,is already registered or not!!
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                # WHAT DOES THE THIS LOGIN DO
                return HttpResponseRedirect(reverse('basic_app:base'))
                # WHAT DOES THE THIS ABOVE CODE DO
                # ###in this value inside reverse is the name of views given in urls.py
                # IF VIEW IS LISTED IN PROJECT FOLDER  URL NAME DIRECTLY WHATEVER NAME IT HAS given
                # return HttpResponseRedirect(reverse('base'))


            else:
                return HttpResponse('Account is not active')
        else:
            print('will show in console')
            print('someone tried to login and faied')
            print('username: {} and password: {}'.format(username,password))
            return HttpResponse('Not registered earlier')
            # return HttpResponseRedirect(reverse('regis'))


    else:
        return render(request,'basic_app/login.html')
