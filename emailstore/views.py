from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from emailstore.forms import EmailForm


def index(request):
    form = EmailForm()
    return render(request, 'home/test-template.html', {'form': form})


def post(request):
    form = EmailForm(request.POST)

    # Form Sanitization (SQL Injection protection) **Undeveloped Feature**
    # if form.is_valid():
    #     form.save()
    #     text = form.cleaned_data['email']
    #     form = EmailForm()
    #     return redirect('home:base')

    # args = {'form': form, 'text': text}
    # return render(request, 'home/base.html', args)
