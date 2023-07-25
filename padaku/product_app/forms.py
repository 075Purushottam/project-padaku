from django.forms import ModelForm
from .models import Enquiry, Feedback

class EnquiryForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
