from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
    word = get_random_string(length=14)
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    context = {
        'count': request.session['counter'],
        'word': word
    }

    return render(request, 'rando_gen/index.html', context)


def generate(request):
    return redirect('/')

def reset(request):
    request.session['counter'] = 0
    return redirect('/')

