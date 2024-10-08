from django.db import transaction
from rest_framework.exceptions import ValidationError


class SaveInsuranceDataService:
    def save_data(self, processed_data):
        user_data = processed_data.get('user_info')
        policy_data = processed_data.get('policy_info')
        plan_data = processed_data.get('plan_info')

        # Using atomic to ensure all operations are treated as a single transaction
        with transaction.atomic():
            # Validate and serialize the user data
            user_serializer = UserInfoSerializer(data=user_data)
            if not user_serializer.is_valid():
                raise ValidationError(user_serializer.errors)
            user = user_serializer.save()

            # Validate and serialize the policy data
            policy_serializer = PolicyInfoSerializer(data=policy_data)
            if not policy_serializer.is_valid():
                raise ValidationError(policy_serializer.errors)
            policy = policy_serializer.save(user=user)

            # Validate and serialize the plan data
            plan_serializer = PlanInfoSerializer(data=plan_data)
            if not plan_serializer.is_valid():
                raise ValidationError(plan_serializer.errors)
            plan_serializer.save(policy=policy)
