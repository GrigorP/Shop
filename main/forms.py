from django.forms import ModelForm
from .models import (
    StayUpdated, BillingAddress,
    ShippingAddress, ContactUs,
    NewsLetter, LeaveReview
    )

class StayUpdatedForm(ModelForm):
    class Meta:
        model = StayUpdated
        fields = '__all__'

class BillingAddressForm(ModelForm):
    class Meta:
        model = BillingAddress
        fields = '__all__'

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        
class NewsLetterForm(ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
        
class LeaveReviewForm(ModelForm):
    class Meta:
        model = LeaveReview
        fields = '__all__'
        
        