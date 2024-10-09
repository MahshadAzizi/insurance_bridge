from django.db import transaction
from rest_framework.exceptions import ValidationError

from insurance_processor.api.serializers import PolicySerializer, PlanSerializer, OrganizationSerializer, \
    InsuredSerializer
from users.api.serializers import UserSerializer


class SaveInsuranceDataService:
    def save_data(self, processed_data):
        user_data = processed_data.get('user_info')
        policy_data = processed_data.get('policy_info')
        plan_data = processed_data.get('plan_info')
        organization_data = processed_data.get('organization_info')
        insurer_data = processed_data.get('insurer_info')
        insured_data = processed_data.get('insured_info')

        # Using atomic to ensure all operations are treated as a single transaction
        with transaction.atomic():
            # Validate and serialize the user data
            user_serializer = UserSerializer(data=user_data)
            if not user_serializer.is_valid():
                raise ValidationError(user_serializer.errors)
            user = user_serializer.save()

            # Validate and serialize the policy data
            policy_serializer = PolicySerializer(data=policy_data)
            if not policy_serializer.is_valid():
                raise ValidationError(policy_serializer.errors)
            policy = policy_serializer.save()

            # Validate and serialize the insurer data
            insurer_serializer = OrganizationSerializer(data=insurer_data)
            if not insurer_serializer.is_valid():
                raise ValidationError(insurer_serializer.errors)
            insurer = insurer_serializer.save()

            # Validate and serialize the plan data
            plan_serializer = PlanSerializer(data=plan_data)
            if not plan_serializer.is_valid():
                raise ValidationError(plan_serializer.errors)
            plan = plan_serializer.save(insurer=insurer)

            # Validate and serialize the organization data
            organization_serializer = OrganizationSerializer(data=organization_data)
            if not organization_serializer.is_valid():
                raise ValidationError(organization_serializer.errors)
            organization = organization_serializer.save()

            insured_serializer = InsuredSerializer(data=insured_data)
            if not insured_serializer.is_valid():
                raise ValidationError(insured_serializer.errors)
            insured_serializer.save(user=user,
                                    policy=policy,
                                    plan=plan,
                                    organization=organization
                                    )
