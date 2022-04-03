from ast import Name
from dataclasses import dataclass
import email
from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Pagina inicial.
def home(request):
    return render  (request,'home.html')


#Formulario de Cadastro de usuario 
def create(request):
    return render  (request,'create.html')


#Inserção dos dados dos usuarios no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'create.html',data)


#Formulario do painel de login
def painel(request):
    return render  (request,'painel.html')

#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username = request.POST['user'], password = request.POST['password'])

    if user is not Name:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuaria ou Senha invalidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html',data)    

#Pagina inicial do dashboard
def dashboard(request):
    return render  (request,'dashboard/home.html')
    
#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')