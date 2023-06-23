from django.contrib.auth.hashers import make_password
from djoser.views import UserViewSet

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.services import markopolo
from django.contrib.auth.models import User
from api.serializers import UserCreateSerializer, UserSerializer
from api.permissions import IsStaffDeleteOrAuth


class UsersViewSet(UserViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    permission_classes = (IsStaffDeleteOrAuth,)

    def get_permissions(self):
        if self.request.method.lower() == 'post':
            return [AllowAny()]
        return [IsStaffDeleteOrAuth()]

    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return UserCreateSerializer
        return UserSerializer

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)


class Service(APIView):
    def post(self, request):
        request_data = request.data.get('numbers')
        if type(request_data) is list:
            print(request_data)
            data = [markopolo(number) for number in request_data]
            return Response({"result": data})
        else:
            data = markopolo(request_data)
            return Response({"result": data})

