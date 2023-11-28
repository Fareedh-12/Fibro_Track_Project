from django.urls import path 
from fibroTrack import views


app_name = 'fibroTrack'


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('daily_fibro_track/', views.daily_fibro_track, name='daily_fibro_track'),
    path('my_fibro_chart/', views.my_fibro_chart, name='my_fibro_chart'),
    path('community_data/', views.community_data, name='community_data'),
]