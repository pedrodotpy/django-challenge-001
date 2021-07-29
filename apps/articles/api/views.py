from django.utils.translation import ugettext_lazy as _
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.articles.models import Article
from .serializers import (
    ArticleSerializer,
    ArticleRetrieveSerializer,
    ArticleListSerializer,
    ArticleAdminSerializer,
)


class ArticleFilter(filters.FilterSet):
    category = filters.CharFilter(method='filter_category', help_text=_('Category\'s slug.'))

    class Meta:
        model = Article
        fields = 'category',

    def filter_category(self, queryset, field_name, value):  # noqa
        return queryset.filter(category__slug=value)


class ArticlePublicViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Article.objects.all().select_related('author', 'category')
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArticleFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        if self.action == 'retrieve':
            return ArticleRetrieveSerializer
        return super().get_serializer_class()


@extend_schema_view(
    # fix conflict with the public article endpoint
    list=extend_schema(operation_id='article_list_admin'),
    retrieve=extend_schema(operation_id='article_retrieve_admin'),
)
class ArticleAdminViewSet(ModelViewSet):
    queryset = Article.objects.all().select_related('author', 'category')
    serializer_class = ArticleAdminSerializer
    permission_classes = [IsAdminUser]
