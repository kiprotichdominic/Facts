from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import InvoiceForm
from .models import Vendor, Buyer, Invoice
from .decorators import unauthenticated_user, allowed_users, vendor_only


@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email =request.POST.get('email')
		password =request.POST.get('password')
  

		user = authenticate(request, username=username, email=email,password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



@login_required(login_url='login')
@vendor_only
def home(request):
	invoices = Invoice.objects.all()
	buyers = Buyer.objects.all()

	total_buyers = buyers.count()

	total_invoices = invoices.count()
	# delivered = invoices.filter(status='Delivered').count()
	# pending = invoices.filter(status='Pending').count()

	context = {'invoices':invoices, 'buyers':buyers,
	'total_invoices':total_invoices}

	return render(request, 'accounts/dashboard.html', context)

def userPage(request):
	invoices = Invoice.objects.all()
	context = {'invoices':invoices}
	return render(request, 'accounts/user.html', context)


class InvoiceCreateView(LoginRequiredMixin ,CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'accounts/invoice.html' 
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)