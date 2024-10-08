from abc import ABC, abstractmethod


class BaseInsuranceHandler(ABC):
    """
    Abstract base class for handling insurance data from different insurers.
    Each insurer will have its own implementation that provides logic for
    processing user info, policy info, plan info, and other insurance-related data.
    """

    @abstractmethod
    def process_user_info(self, user_data):
        """
        Process and validate user information.
        :param user_data: Dict containing user-related information.
        :return: Processed user data, ready to be saved.
        """
        pass

    @abstractmethod
    def process_policy_info(self, policy_data):
        """
        Process and validate policy information.
        :param policy_data: Dict containing policy-related information.
        :return: Processed policy data, ready to be saved.
        """
        pass

    @abstractmethod
    def process_plan_info(self, plan_data):
        """
        Process and validate plan information.
        :param plan_data: Dict containing plan-related information.
        :return: Processed plan data, ready to be saved.
        """
        pass

    def process_insurance_data(self, data):
        """
        Main method that coordinates the processing of insurance data. This ensures
        that the steps are followed in the correct order (first user info, then policy info, etc.)
        and consolidates error handling.
        :param data: The complete insurance data (JSON) from the insurer.
        :return: Processed data for user info, policy info, and plan info.
        """
        # Extract individual parts of the insurance data
        user_info = data.get('user_info')
        policy_info = data.get('policy_info')
        plan_info = data.get('plan_info')

        # Process each part using the specific methods
        processed_user_info = self.process_user_info(user_info)
        processed_policy_info = self.process_policy_info(policy_info)
        processed_plan_info = self.process_plan_info(plan_info)

        # Return the processed data in a structured format
        return {
            'user_info': processed_user_info,
            'policy_info': processed_policy_info,
            'plan_info': processed_plan_info,
        }
