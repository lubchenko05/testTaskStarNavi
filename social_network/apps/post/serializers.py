from rest_framework import serializers

from apps.user.serializers import UserPreviewSerializer
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    author = UserPreviewSerializer(read_only=True)
    likes = UserPreviewSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'author', 'likes')
