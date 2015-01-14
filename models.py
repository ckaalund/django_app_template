from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from apps.my_model.managers import MyModelManager


class MyModel(models.Model):
    # name = models.CharField(max_length=255, blank=True)
    # is_active = models.BooleanField(default=True)
    # created = models.DateTimeField(default=timezone.now)

    # objects = MyModelManager()

    # class Meta:
    #     ordering = ['-created']
    #     verbose_name = _('model')
    #     verbose_name_plural = _('models')

    # def __unicode__(self):
    #     return self.name
