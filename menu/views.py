from django.shortcuts import render
from .models import MenuTree


def menu(request):
    return render(request, 'menu/menu.html', {
        'menu': MenuTree.objects.all()
    })
