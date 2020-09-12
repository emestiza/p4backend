from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# not all models need CRUD; sometimes all we need to do is read only
from rest_framework.viewsets import ReadOnlyModelViewSet
# we can allow all the users to see this view
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, LoginSerializer, UserListSerializer
from .models import User

class RegistrationAPIView(APIView):
    # allows any user to hit this endpoint
    permission_classes = (AllowAny,)  # allows anyone to register at this endpoint
    serializer_class = RegistrationSerializer

    #new version
    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "email": request.data.get('email'),
                "username": request.data.get('username'),
                "password": request.data.get('password'),
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # first version
    """
    def post(self, request):  # post instead of create bc inheriting method from APIView
        user = request.data.get('user', {})  # empty {} bc by default object is empty; populate with acquired info
        if not user:
            user = {
                "username": request.data.get('username'),  # req is dict, so accessing key username
                "password": request.data.get("password")
            }

        # converting the data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    """


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)  # COMMA IS A MUST to make it a tuple of one or more items
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

