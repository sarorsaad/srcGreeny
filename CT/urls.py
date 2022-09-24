from django.urls import path
from .views import HospitalList
# from django.views.generic import TemplateView

app_name='CT'

urlpatterns = [
   path("", HospitalList.as_view(), name="Hospital_list"),  


]