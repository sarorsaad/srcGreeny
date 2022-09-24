from django.db import models
from django.utils.translation import gettext as _



class Hospital(models.Model):

    # Fields
  
    name = models.CharField(_('Name'), max_length=30)
    Deparment = models.CharField(_('Deparment '),max_length=30)
    Region = models.CharField(_('Region '),max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

