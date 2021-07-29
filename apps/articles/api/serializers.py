from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from apps.articles.models import Article
from apps.authors.api.serializers import AuthorSerializer
from challenge.helpers import PrivateFieldsSerializerMixin


class ArticleAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ()


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = 'id', 'author', 'category', 'title', 'summary',


class ArticleListSerializer(ArticleSerializer):
    category = serializers.StringRelatedField(help_text=_('Category\'s name'))
    author = AuthorSerializer()


class ArticleRetrieveSerializer(PrivateFieldsSerializerMixin, ArticleListSerializer):
    private_fields = 'body',

    class Meta(ArticleListSerializer.Meta):
        fields = ArticleSerializer.Meta.fields + ('first_paragraph', 'body')
