from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.models import AutoSlugField

from challenge.helpers import BaseModelMixin


class Category(BaseModelMixin):
    name = models.CharField(_('name'), max_length=20, unique=True)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = 'name',

    def __str__(self):
        return self.name
