from django.shortcuts import render


def index(request):
    print('Entro al index')
    return render(request, template_name='landingpage/index.html')
