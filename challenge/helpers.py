import os
import uuid

from django.db import models
from django.db.models.deletion import ProtectedError
from django.utils.text import format_lazy
from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import ValidationError


class BaseModelMixin(models.Model):
    """Override the default primary key and add timestamps fields"""
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(_('created at'), null=False, blank=True, auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('updated at'), null=False, blank=True, auto_now=True, editable=False)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        try:
            return super().delete(using, keep_parents)
        except ProtectedError:
            raise ValidationError(
                format_lazy(
                    _('Cannot delete. The {obj_name} is being referenced by one or more entities.'),
                    obj_name=self._meta.verbose_name
                )
            )


class PrivateFieldsSerializerMixin:
    """
    Conditionally removes the provided fields if the user is not authenticated.

    The use of the help_text if important for drf-spectacular's schema generator
    to inform the behavior of the private fields.
    """
    private_fields = None
    private_fields_help_text = _('Included only if the user is authenticated.')

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request', None)
        if request and request.user.is_anonymous:
            [fields.pop(field) for field in self.private_fields or []]
        else:  # The request is not present in the context when drf-spectacular analyses the serializer
            for field in self.private_fields:
                fields[field].help_text = self.private_fields_help_text
        return fields


def get_upload_path(instance, filename) -> str:
    """Upload path for media files. The folder name is the instance's class name, the file name is a uuid4 string"""
    _, file_extension = os.path.splitext(filename)
    new_filename = uuid.uuid4()
    return os.path.join(instance.__class__.__name__.lower(), f'{new_filename}{file_extension}')
