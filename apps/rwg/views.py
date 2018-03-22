# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    # response = "This is the localhost:8000 (rwg index) page"
    # return HttpResponse(response)
    context = {
        "random": get_random_string(length=14)
    }
    if request.method == "POST":
        if "counter" not in request.session:
            request.session["counter"] = 0
        else:
            request.session["counter"] += 1
    print request.session["counter"]
    return render(request, 'index.html', context)

def random_words(request):
    response = "This is the localhost:8000 (random_words) page"
    return HttpResponse(response)