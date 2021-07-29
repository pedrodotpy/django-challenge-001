from rest_framework import serializers

from apps.authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = 'created_at', 'updated_at'
