from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class UserCreateView(APIView):
    """
    Creates the user.
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                from rest_framework import status
                return Response(serializer.data, status=status.HTTP_201_CREATED)
