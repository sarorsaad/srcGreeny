from django import forms
from . import models


class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = [
            "MRN",
            "Nationality",
            "Name",
            "Age",
        ]