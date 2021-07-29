from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.categories.models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
