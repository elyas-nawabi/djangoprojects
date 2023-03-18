import json
import urllib.request
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
import requests
from .models import *
from .forms import ImageForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def counter(request):
    return render(request, 'words.html')


def handleCounter(request):
    words = request.POST['words']
    counter = len(words.split())
    return render(request, 'handleCounter.html', {'words': counter})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def handleRegister(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('handleRegister')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('handleRegister')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not the same')
            return redirect('handleRegister')
    else:
        return render(request, 'handleRegister.html')


def reg(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used.')
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('reg')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password is not the same')
            return redirect('reg')
    else:
        return render(request, 'reg.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


# def posts(request):
#     posts = Post.objects.all()
#     return render(request, 'posts.html', {'posts': posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_details.html', {'post': post})


# def weather(request):
#     if request.method == 'POST':
#         city = request.POST['city']
#         response = requests.get(
#             'http://api.weatherapi.com/v1/current.json?key=18ca45c7e407473a92182113231303&q='+city+'&aqi=no')
#         data = response.json()
#         data = {
#             "country_code": data['location']['name'],
#             "coordinate": data['location']['lat'] + data['location']['lon'],
#             "temp": data['current']['temp_f'],
#             "pressure": data['current']['pressure_mb'],
#             "humidity": data['current']['humidity'],
#         }
#     else:
#         data = {}
#     return render(request, 'weather.html', data)

def weather(request):
    if request.method == "POST":
        city = request.POST['city']
        response = requests.get(
            'http://api.weatherapi.com/v1/current.json?key=18ca45c7e407473a92182113231303&q='+city+'&aqi=no')
        data = response.json()
        data = {
            "country_code": data['location']['name'],
            "coordinate": data['location']['lat'] + data['location']['lon'],
            "temp": data['current']['temp_f'],
            "pressure": data['current']['pressure_mb'],
            "humidity": data['current']['humidity'],
            "cloud": data['current']['cloud'],
        }
    else:
        data = {}
    return render(request, 'weather.html', data)


def users(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    # convert reponse data into json
    users = response.json()
    # print(users)
    return render(request, "users.html", {'users': users})


def list_users(request):
    data = requests.get('https://jsonplaceholder.typicode.com/users')
    users = data.json()
    return render(request, 'users.html', {'users': users})


def chat(request):
    return render(request, 'chat.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})


def imageupload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'imageupload.html', {'img': img, 'form': form})
