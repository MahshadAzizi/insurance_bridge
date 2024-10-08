import importlib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from insurance_processor.services import SaveInsuranceDataService


class InsuranceDataView(APIView):
    def post(self, request):
        # Assume we have a field in the request body indicating the insurance company
        insurance_company = request.data.get('insurance_company')

        if not insurance_company:
            return Response({"error": "Insurance company not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Dynamically import the handler based on the insurance company name
            handler_module = importlib.import_module(f'insurance_api.handlers.{insurance_company.lower()}_handler')
            handler_class = getattr(handler_module, f'{insurance_company.capitalize()}InsuranceHandler')

            # Instantiate the handler
            handler = handler_class()

        except (ImportError, AttributeError) as e:
            return Response({"error": f"Handler for {insurance_company} not found."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Process the data using the handler
        try:
            processed_data = handler.process_insurance_data(request.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Pass the processed data to the service to handle saving
        insurance_data_service = SaveInsuranceDataService()

        try:
            insurance_data_service.save_data(processed_data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Data processed and saved successfully."}, status=status.HTTP_201_CREATED)
