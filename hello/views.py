from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from .models import Greeting, Product

# Create your views here.
def index(request):

    # return HttpResponse('Hello from Python!')
    p = Product(id=1)
    variables = {
        'p':p
    }
    return render_to_response('index.html', variables)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

