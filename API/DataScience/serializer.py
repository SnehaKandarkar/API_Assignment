from rest_framework import serializers
from.models import ComputerScienceModel


class ComputerScienceSer(serializers.ModelSerializer):
    class Meta:
        model = ComputerScienceModel
        fields = "__all__"