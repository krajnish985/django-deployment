from django.urls import path

from basic_app import views


app_name="basic_app"

urlpatterns = [
    path('base/',views.basic,name='base'),
    
    path('login/',views.user_login,name="login"),
    path('register/',views.registeration,name='registeration'),
    path('special/',views.special,name='special'),

]
