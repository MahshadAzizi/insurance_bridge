from insurance_processor.handlers import BaseInsuranceHandler


class MelatInsuranceHandler(BaseInsuranceHandler):

    def process_user_info(self, user_data):
        # Example: Map Melat's keys to the internal format
        processed_user_info = {
            'first_name': user_data.get('first_name'),
            'last_name': user_data.get('last_name'),
        }
        return processed_user_info

    def process_policy_info(self, policy_data):
        # Process policy info specific to Melat
        processed_policy_info = {
            'policy_id': policy_data.get('policy_id'),
            'start_date': policy_data.get('start_date'),
            'end_date': policy_data.get('end_date'),
        }
        return processed_policy_info

    def process_plan_info(self, plan_data):
        # Process plan info specific to Melat
        processed_plan_info = {
            'plan_name': plan_data.get('plan_name'),
            'plan_id': plan_data.get('plan_id'),
        }
        return processed_plan_info
