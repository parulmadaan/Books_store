from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from Author.forms import RegistrationForm
from Author.forms import sendemailForm
from Author.forms import LogInForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template.loader import get_template
from book_store.settings import TEMPLATES
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from .models import User
import os



def index(request):
    return render(request, 'author/email.html')


def logo_data():
    with open(finders.find(os.path.join(settings.BASE_DIR,'static/images/book.jfif')), 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data)
    # logo.add_header('Content-ID', '<logo>')
    logo.add_header('Content-ID', "<{logo}>")
    return logo


def registration_view(request):

    if request.method == 'POST':
        print("-->", request.POST.get('firstname'))
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        image = request.POST.get('image')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        content = request.POST.get('content')

        user = User.objects.create_user(
            first_name=fname, last_name=lname, avatar=image, email=email, password=password1)
        User.is_staff = True
        login(request, user)
        subject = 'Welcome to Book Store!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        htmltemp = render_to_string('author/email.html')
        text_content = strip_tags(htmltemp)
        msg = EmailMultiAlternatives(subject,text_content,email_from, recipient_list,)
        msg.mixed_subtype = 'related'
        msg.attach_alternative(htmltemp, "text/html")
        msg.attach(logo_data())
        msg.send()
        return redirect("login")

    return render(request, "author/registration.html", {"form": "Registration"})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        request.session['user_id'] = user.id
        request.session['user_email'] = user.email
        user_data = User.objects.get(email=username)
        return render(request,'author/userhome.html',{"userData": user_data, "loginUser": user})
    return render(request, 'author/login.html')

def profile_page(request):
    loginUser = request.user
    return render(request,'author/profile.html',{"loginUser": loginUser})



def home_page(request):
    loginUser = request.user
    return render(request, 'author/home.html')


def logout_link(request):
    logout(request)
    loginUser = None
    return redirect("login")