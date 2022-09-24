from django.views.generic import ListView

from.models import Patient
# from . import forms

# Create your views here.
class PatientList(ListView):
    model = Patient