from rest_framework import serializers

from insurance_processor.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'name',
            'organisation_id',
            'created_at'
        ]
