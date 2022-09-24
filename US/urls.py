from django.urls import path
from .views import PatientList
# from django.views.generic import TemplateView



urlpatterns = [
   path("", PatientList.as_view(), name="Patient_list"),  


]