from django.db import models
from django.utils.translation import ugettext as _

from challenge.helpers import BaseModelMixin
from challenge.helpers import get_upload_path


class Author(BaseModelMixin):
    name = models.CharField(_('name'), max_length=50)
    picture = models.ImageField(_('picture'), upload_to=get_upload_path, blank=True)

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
        ordering = 'name',

    def __str__(self):
        return self.name
