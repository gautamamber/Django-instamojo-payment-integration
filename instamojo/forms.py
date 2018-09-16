from django import forms

class PaymentForm(forms.Form):
	name = forms.CharField(label = "Name", max_length = 30)
	email = forms.EmailField(label = "Email")
	contact_no = forms.IntegerField(label = "Your contact no" , )
	amount = forms.IntegerField(label = "Amount")
	purpose = forms.CharField(label = "Purpose" , max_length = 200)
