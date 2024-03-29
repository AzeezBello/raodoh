from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.template.loader import render_to_string
from .models import User
from .forms import UserForm, ProfileForm
from .tokens import account_activation_token
from django.db import transaction


# Create your views here.
def index(request):

    return render(request, 'home/index.html', {})


def thanks(request):

    return render(request, 'home/thanks.html', {})


def upload(request):

    return render(request, 'home/upload.html', {})


def activation_sent(request):

    return render(request, 'registration/activation_sent.html', {})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    else:
        return render(request, 'registration/activation_invalid.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Raodoh Account'
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')

    else:
        form = UserForm()

    return render(request, 'registration/signup.html', {'form': form})


def profile(request):

    return render(request, 'registration/profile.html', {'user': request.user})


@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        form = ProfileForm(request.POST, instance=request.user)
        if user_form.is_valid() and form.is_valid():
            user_form.save()
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')

        else:
            messages.error(request, 'Please correct the error below.')

    else:
        user_form = UserForm(instance=request.user)
        form = ProfileForm(instance=request.user)

    return render(request, 'registration/edit_profile.html', {
        'user_form': user_form,
        'form': form
    })

