from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.user.permissions import IsPostOrIsAuthenticated
from .serializers import UserSerializer, UserPreviewSerializer


class UserCreateView(APIView):
    permission_classes = (IsPostOrIsAuthenticated, )

    def get(self, request):
        serializer = UserPreviewSerializer(request.user)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
