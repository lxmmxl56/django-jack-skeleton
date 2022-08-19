import logging

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import HttpResponse, redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

from .forms import SignUpForm
from .token import account_activation_token

log = logging.getLogger(settings.DEBUG_LOGGER)


def signup(request):
    if request.method == 'POST':
        log.debug('POST')
        form = SignUpForm(request.POST)
        if form.is_valid():
            log.debug('valid')
            log.debug(form.cleaned_data.get('email', None))
            try:
                user = User.objects.get(email=form.cleaned_data.get('email', None))
            except User.DoesNotExist:
                user = form.save(commit=False)
                user.username = user.email
                user.is_active = False
                user.save()
            current_site = get_current_site(request)
            subject = _('Activate Your Account')
            message = render_to_string(
                'account/mail/activation_email.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                },
            )
            user.email_user(subject, message)
            return redirect('activation_sent')
        else:
            log.debug('invalid')
            return render(request, 'account/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'account/signup.html', {'form': form})


def activation_sent(request):
    return render(request, 'account/activation_sent.html')


def activation_success(request):
    return render(request, 'account/activation_success.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        return redirect('activation_success')
    else:
        return render(request, 'account/activation_invalid.html')


@login_required
def profile(request):
    return render(request, 'account/profile.html')
