from django.urls import path
from insurance_processor.api.views import InsuranceDataView

urlpatterns = [
    path('', InsuranceDataView.as_view(), name='insurance_data')

]
