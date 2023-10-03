from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.contrib import messages

def criar_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_created = get_user_model().objects.create(
            email=email
        )
        user_created.set_password(password)
        user_created.save()
        messages.success(request, f'Usuário cadastrado com sucesso.')


    return render(request, 'criar_cliente.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(
            username=email,
            password=password
        )
        if user:
            login(request, user)
            messages.success(request, f'Bem vindo {user.email}')
            return redirect('produtos:listar_produtos')
        else:
            messages.info(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('produtos:listar_produtos')