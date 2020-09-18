from django.urls import path
from blog import views

urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('posts/<int:id>', views.PostDetailView.as_view()),
]
