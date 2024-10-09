from rest_framework import serializers

from insurance_processor.models import Insurer


class InsurerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurer
        fields = [
            'name',
            'insurer_unique_id',
            'created_at'
        ]
