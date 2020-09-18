from django.urls import path
from accounts import views

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('users', views.UserView.as_view()),
]
