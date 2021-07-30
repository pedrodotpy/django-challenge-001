from django.db import models
from django.utils.translation import ugettext as _

from challenge.helpers import BaseModelMixin


class Category(BaseModelMixin):
    name = models.CharField(_('name'), max_length=20, unique=True)
    slug = models.CharField(_('slug'), max_length=40, editable=False, unique=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = 'name',

    def __str__(self):
        return self.name
