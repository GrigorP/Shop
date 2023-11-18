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
        

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
        