from users.models import User
from rest_framework import viewsets, status
from users.serliazers import UserSerializer
from rest_framework.response import Response
from users.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        """
        Ограничения режимами доступа
        """
        if self.action == 'create':
            self.permission_classes = []
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            self.permission_classes = [IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner]

        return [permission() for permission in self.permission_classes]

    def create(self, request):
        """
        Создание пользователя
        :param request:
        :return:
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
