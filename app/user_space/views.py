from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.template import loader
from .models import Dog


def index(request):
    dogs_list = Dog.objects.all()
    template = loader.get_template('user/index.html')
    context = {
        'dogs_list': dogs_list,
    }
    return render(request, 'user/index.html', context)


def detail(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'user/detail.html', {'dog': dog})


def login(request):
    return render(request, 'user/login.html')
