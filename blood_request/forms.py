from django.contrib.auth.forms import forms
from blood_request.models import Blood_request

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = Blood_request
        fields = [
            'patient_name',
            'blood_group',
            'blood_amount',
            'request_address',
            'request_purpose',
            'special_notes',
        ]
