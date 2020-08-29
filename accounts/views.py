from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from .form import SignUpForm
from .models import CustomUser


def login(request):
    """
    This function verify post request and also apply different kind of validation like required field,
    email validation, active or inactive user etc.
    Once user required info is validated then allow to login successfully and redirect to home page.
    :param request:
    :return:
    """
    if request.method == 'POST':
        if "email" in request.POST and "password" in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            is_user = CustomUser.objects.filter(email=email)
            if is_user.exists():
                get_user = CustomUser.objects.get(email=email)
                if get_user.is_active:
                    user = authenticate(email=email, password=password)
                    if user is not None:
                        if user.is_active:
                            auth_login(request, user)
                            return redirect('home')
                        else:
                            messages.error(request, "You're accounts is disabled. Contact Admin!")
                    else:
                        messages.error(request, "Invalid login credentials!")
                else:
                    messages.error(request, "Your Account Is Disable. Contact Admin For Activate Your Account!")
            else:
                messages.error(request, "Email ID is not exists!")
        else:
            messages.error(request, "Please provide email and password to do login!")
    return render(request, 'login.html')


def signup(request):
    """
    This function validate user registration form required field.
    if required information match then allow to register and login in
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
