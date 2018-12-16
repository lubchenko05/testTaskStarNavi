from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostListSerializer
from .models import Post

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostListSerializer
    queryset = Post.objects.all()

    def post(self, request):
        serializer = PostListSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            if post:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'])
    def like(self, request, pk=None):
        post = self.get_object()
        if not request.user in post.likes.all():
            post.likes.add(request.user)
            post.save()
            return Response({'detail': 'Like was successfully passed.'})
        else:
            return Response(
                {'detail': _('This post was already liked,')},
                status=status.HTTP_400_BAD_REQUEST
             )

    @action(detail=True, methods=['get'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            post.save()
            return Response({'detail': 'Like was removed successfully.'})
        else:
            return Response(
                {'detail': _('User did not like this post before.')},
                status=status.HTTP_400_BAD_REQUEST
             )
