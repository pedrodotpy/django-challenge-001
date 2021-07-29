from django.db import models
from django.utils.translation import ugettext as _

from challenge.helpers import BaseModelMixin


class Article(BaseModelMixin):
    author = models.ForeignKey(
        'authors.Author',
        verbose_name=_('author'),
        related_name='articles',
        related_query_name='articles',
        on_delete=models.PROTECT
    )
    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('category'),
        related_name='articles',
        related_query_name='articles',
        on_delete=models.PROTECT
    )
    title = models.CharField(_('title'), max_length=120)
    summary = models.TextField(_('summary'))
    first_paragraph = models.TextField(_('first paragraph'))
    body = models.TextField(_('body'))

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = '-created_at',

    def __str__(self):
        return self.title
