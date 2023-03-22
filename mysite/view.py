from django.shortcuts import render


def error_404(request):
    template_name = '404.html'
    return render(request, template_name)