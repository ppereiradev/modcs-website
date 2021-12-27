from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import PasswordResetForm
from .forms import LoginForm
from django.contrib import messages
from django.urls import reverse
from .models import User

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

import os

# Create your views here.
def log_in(request):

    if request.user.is_authenticated:
        return redirect('dashboards:index')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # We check if the data is correct
            user = authenticate(email=email, password=password)
            if user:  # If the returned object is not None
                login(request, user)  # we connect the user
                messages.success(request, "Bem-vindo " + str(user))
                return redirect('dashboards:index')
            else:  # otherwise an error will be displayed
                messages.error(request, 'Email ou senha inválida')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def log_out(request):
    logout(request)

    return redirect(reverse('accounts:login'))


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Recuperar senha acesso ao Dashboard da Divisão de Soluções para Campus Inteligente - DSCI"
					email_template_name = "accounts/password_reset_email.html"
					c = {
					"email":user.email,
					'domain':os.getenv('DOMAIN'),
					'site_name': 'Dashboard - Divisão de Soluções para Campus Inteligente',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, os.getenv('EMAIL_HOST_USER'), [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("done/")
					
	password_reset_form = PasswordResetForm()
	return render(request, 'accounts/password_reset.html', {'password_reset_form': password_reset_form})
    