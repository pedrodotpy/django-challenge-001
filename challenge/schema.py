from django.utils.translation import ugettext_lazy as _
from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import serializers

"""
Override library's views and serializers definitions for the schema generation
https://drf-spectacular.readthedocs.io/en/latest/customization.html#step-5-extensions
"""


class FixRegisterView(OpenApiViewExtension):
    target_class = 'rest_auth.registration.views.RegisterView'

    def view_replacement(self):
        sign_up_error = inline_serializer(
            'SignUpFailed', {'field_name': serializers.ListField(child=serializers.CharField(), help_text=_('Errors'))}
        )

        @extend_schema(
            responses={
                200: OpenApiResponse(response=self.target_class.serializer_class, description=_('Created user')),
                400: OpenApiResponse(response=sign_up_error)
            }
        )
        class Fixed(self.target_class):
            pass

        return Fixed


class FixLoginViewiew(OpenApiViewExtension):
    target_class = 'rest_auth.views.LoginView'

    def view_replacement(self):
        serializer = inline_serializer(
            'LoginSerializer',
            {'username': serializers.CharField(), 'password': serializers.CharField()}
        )

        response_serializer = inline_serializer(
            'LoginResponseSerializer',
            {'key': serializers.CharField(help_text=_('Authentication token.'))}
        )

        response_error_serializer = inline_serializer(
            'LoginFailedSerializer',
            {'nonFieldErrors': serializers.ListField(child=serializers.CharField())}
        )

        @extend_schema(
            request=serializer,
            responses={
                200: OpenApiResponse(response=response_serializer, description=_('Authentication token.')),
                400: OpenApiResponse(response=response_error_serializer, description=_('List of errors.')),
            }
        )
        class Fixed(self.target_class):
            serializer_class = serializer

            @extend_schema(exclude=True)
            def get(self, request):
                pass

        return Fixed


class FixLogoutViewiew(OpenApiViewExtension):
    target_class = 'rest_auth.views.LogoutView'

    def view_replacement(self):
        serializer = inline_serializer(
            'LogoutSerializer',
            {'detail': serializers.CharField(help_text=_('Success message.'))}
        )

        @extend_schema(
            request=None,
            responses=OpenApiResponse(response=serializer, description=_('Successfully logged out.'))
        )
        class Fixed(self.target_class):
            serializer_class = serializer

            @extend_schema(exclude=True)
            def get(self, request):
                pass

        return Fixed
