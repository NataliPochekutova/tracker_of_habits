from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet для полного CRUD пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserListApiView(generics.ListAPIView):
    """API-View для получения списка всех пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveApiView(generics.RetrieveAPIView):
    """API-View для получения данных конкретного пользователя по его идентификатору"""

    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    """API-View для создания нового пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserUpdateApiView(generics.UpdateAPIView):
    """API-View для обновления существующего пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyApiView(generics.DestroyAPIView):
    """API-View для удаления пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
