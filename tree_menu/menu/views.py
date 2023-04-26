from django.shortcuts import render

from .models import Menu


def index(request):
    menus = Menu.objects.all().values('title')
    context = {
        'menus': menus
    }
    return render(request, 'menu/index.html', context)
