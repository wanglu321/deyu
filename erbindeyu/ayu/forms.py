from django.forms import ModelForm
from .models import Message


# Code added for loading form data on the Booking page
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        
