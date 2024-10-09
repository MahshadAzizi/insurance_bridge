from insurance_processor.handlers import BaseInsuranceHandler


class PasargadInsuranceHandler(BaseInsuranceHandler):

    def process_user_info(self, user_data):
        # Example: Map Pasargad's keys to the internal format
        processed_user_info = {
            'first_name': user_data.get('first_name'),
            'last_name': user_data.get('last_name'),
            'email': user_data.get('email'),
            'father_name': user_data.get('father_name'),
            'national_code': user_data.get('national_code'),
            'place_of_issue': user_data.get('place_of_issue'),
            'mobile_number': user_data.get('mobile_number'),
            'birth_date': user_data.get('birth_date'),
            'created_at': user_data.get('created_at'),
        }
        return processed_user_info

    def process_policy_info(self, policy_data):
        # Process policy info specific to Pasargad
        processed_policy_info = {
            'policy_id': policy_data.get('policy_id'),
            'policy_start_date': policy_data.get('start_date'),
            'policy_end_date': policy_data.get('end_date'),
            'policy_unique_id': policy_data.get('unique_id'),
            'confirmation_date': policy_data.get('confirmation_date'),
            'created_at': policy_data.get('created_at'),
        }
        return processed_policy_info

    def process_plan_info(self, plan_data):
        # Process plan info specific to Pasargad
        processed_plan_info = {
            'name': plan_data.get('name'),
            'created_at': plan_data.get('created_at'),
        }
        return processed_plan_info

    def process_organization_info(self, organization_data):
        # Process or organization specific to Pasargad
        process_organization_info = {
            'name': organization_data.get('name'),
            'organisation_id': organization_data.get('organisation_id'),
            'created_at': organization_data.get('created_at'),
        }
        return process_organization_info

    def process_insurer_info(self, insurer_data):
        # Process or insurer specific to Pasargad
        process_insurer_info = {
            'name': insurer_data.get('name'),
            'insurer_unique_id': insurer_data.get('insurer_unique_id'),
            'created_at': insurer_data.get('created_at'),
        }
        return process_insurer_info

    def process_insured_info(self, insured_data):
        # Process or insurer specific to Pasargad
        process_insured_info = {
            'insured_id': insured_data.get('insured_id'),
        }
        return process_insured_info
