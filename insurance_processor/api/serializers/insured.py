from rest_framework import serializers

from insurance_processor.models import Insured


class InsuredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insured
        fields = [
            'insured_id',
        ]
