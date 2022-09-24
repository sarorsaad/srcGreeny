from rest_framework import serializers

from . import models


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Patient
        fields = [
            "created",
            "MRN",
            "Nationality",
            "last_updated",
            "Name",
            "Age",
        ]