from django.db import models
from django.utils.translation import gettext as _




class Patient(models.Model):

    # Fields
    Nationality = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    MRN = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)
