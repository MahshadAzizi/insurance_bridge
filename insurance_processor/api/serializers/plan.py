from rest_framework import serializers

from insurance_processor.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = [
            'name',
            'insurer',
            'created_at'
        ]
