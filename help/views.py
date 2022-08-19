from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import HelpSection


def help(request):
    return render(
        request,
        'help.html',
        {
            'section': 'help',
            'sections': HelpSection.objects.all(),
        },
    )
