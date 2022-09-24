
from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PatientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Patient class"""

    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    permission_classes = [permissions.IsAuthenticated]