
from django.views.generic import ListView

from.models import Hospital
# from . import forms

# Create your views here.
class HospitalList(ListView):
    model = Hospital
    

