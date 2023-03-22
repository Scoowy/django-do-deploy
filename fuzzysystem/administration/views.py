from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse


def login(request):
    method = request.method

    if method == 'POST':
        # obtener el nombre de usuario y la contraseña del formulario de inicio de sesión
        username = request.POST['username']
        password = request.POST['password']

        print(f'Username: {username} Pass: {password}')

        credentials = {
            'username': username,
            'password': password
        }

        # User authentication
        user = authenticate(request, **credentials)
        print(f'User: {user}')

        if user is None:
            context = {
                'error_msg': 'El nombre de usuario o la contraseña son incorrectos.'
            }

            return render(request, 'administration/login.html', context)

        # Init sesion
        auth_login(request, user)
        return redirect(reverse('upload'))

    else:
        return render(request, 'administration/login.html')
