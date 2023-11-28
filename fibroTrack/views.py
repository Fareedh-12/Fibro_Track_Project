from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def index(request):
    return render(request, "fibroTrack/index.html")

def signup(request):
    return HttpResponse("Hello, world. You're at the fibroTrack signup.")

def login(request):
    return HttpResponse("Hello, world. You're at the fibroTrack login.")

def daily_fibro_track(request):
    return HttpResponse("Hello, world. You're at the fibroTrack daily_fibro_track.")

def my_fibro_chart(request):
    return HttpResponse("Hello, world. You're at the fibroTrack my_fibro_chart.")

def community_data(request):
    return HttpResponse("Hello, world. You're at the fibroTrack community_data.")
