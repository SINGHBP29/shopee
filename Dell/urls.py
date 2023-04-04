
from django.urls import path
from . import views
#import authentication.views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.login, name="Login"),
    path("register/",views.register, name="Register"),
    path('tesonomial/',views.testonomial,name="Testonomial"),
    path('signout/',views.signout, name="signout"),
    path('dashboard/', views.dashboard, name="dashboard"),
]