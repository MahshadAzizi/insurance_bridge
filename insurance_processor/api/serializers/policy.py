from rest_framework import serializers

from insurance_processor.models import Policy


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = [
            'policy_start_date',
            'policy_end_date',
            'policy_unique_id',
            'confirmation_date',
            'created_at'
        ]
