from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.authors.models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]
