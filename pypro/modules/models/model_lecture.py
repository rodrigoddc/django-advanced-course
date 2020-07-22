from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel

from pypro.modules.models import Module


class Lecture(OrderedModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    module = models.ForeignKey(Module, on_delete=models.PROTECT)
    order_with_respect_to = 'module'

    class Meta(OrderedModel.Meta):
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('modules:lecture_detail', kwargs={'slug': self.slug})
