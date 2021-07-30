from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .models import Category


@receiver(pre_save, sender=Category)
def category_pre_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
