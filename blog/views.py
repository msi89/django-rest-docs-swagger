from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework import permissions


class PostList(ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)
