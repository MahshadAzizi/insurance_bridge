from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'father_name',
            'national_code',
            'place_of_issue',
            'mobile_number',
            'birth_date',
            'created_at'
        ]
