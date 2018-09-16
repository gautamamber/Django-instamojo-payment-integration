from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from instamojo_wrapper import Instamojo
from  django.urls import reverse
from .forms import PaymentForm
# Create your views here.
# def index(request):
# 	return HttpResponse("Hello world")

payment_api = Instamojo(api_key = "-----your api key--------" , auth_token = "---------your auth token-------------------", endpoint='https://test.instamojo.com/api/1.1/')

def index(request):
	if request.method == 'POST':
		print("\n\n" + str(request.POST))
		form = PaymentForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			response = payment_api.payment_request_create(
				amount = str(data['amount']),
				purpose = data['purpose'],
				send_email = False,
				send_sms = False,
				email = data['email'],
				buyer_name = data['name'],
				phone = data['contact_no'],
				redirect_url = request.build_absolute_uri(reverse('www.xyz.com'))
				)
				
			return HttpResponseRedirect(response['payment_request']['longurl'])

	else:
		form = PaymentForm()
		
	return render(request, 'instamojo/payment.html', {'form' :form})




