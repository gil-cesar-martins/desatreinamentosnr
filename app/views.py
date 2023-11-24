from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Página Incial
def home(request):
    return render(request, 'home.html')

#Formulário de Cadastro de Usuários
def create(request):
    return render(request, 'create.html')

#Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.last_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'create.html',data)

#Formulário do painel de Login
def painel(request):
    return render(request, 'painel.html')

#Processa o Login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/treinamentos/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)

#Página inicial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')

#Página dos treinamentos
def treinamentos(request):
    return render(request, 'treinamentos.html')

#Página do treinamento NR01
def treinamentos01(request):
    return render(request, 'treinamentos01.html')

#Página do treinamento NR06
def treinamentos06(request):
    return render(request, 'treinamentos06.html')

#Página do treinamento NR12
def treinamentos12(request):
    return render(request, 'treinamentos12.html')

#Página do treinamento NR17
def treinamentos17(request):
    return render(request, 'treinamentos17.html')

#Página do treinamento NR18-andaimes
def treinamentos18andaimes(request):
    return render(request, 'treinamentos18-andaimes.html')

#Página do treinamento NR18-soldagem
def treinamentos18soldagem(request):
    return render(request, 'treinamentos18-soldagem.html')

#Página do treinamento NR20
def treinamentos20(request):
    return render(request, 'treinamentos20.html')

#Página do treinamento NR33
def treinamentos33(request):
    return render(request, 'treinamentos33.html')

#Página do treinamento NR34
def treinamentos34(request):
    return render(request, 'treinamentos34.html')

#Página do treinamento NR35
def treinamentos35(request):
    return render(request, 'treinamentos35.html')


#Página dos videos NR01
def videos01(request):
    return render(request, 'videos01.html')

#Página dos videos NR06
def videos06(request):
    return render(request, 'videos06.html')

#Página dos videos NR12
def videos12(request):
    return render(request, 'videos12.html')

#Página dos videos NR17
def videos17(request):
    return render(request, 'videos17.html')

#Página dos videos NR18 andaimes
def videos18andaimes(request):
    return render(request, 'videos18-andaimes.html')

#Página dos videos NR18 soldagem
def videos18soldagem(request):
    return render(request, 'videos18-soldagem.html')

#Página dos videos NR20
def videos20(request):
    return render(request, 'videos20.html')

#Página dos videos NR33
def videos33(request):
    return render(request, 'videos33.html')

#Página dos videos NR34
def videos34(request):
    return render(request, 'videos34.html')

#Página dos videos NR35
def videos35(request):
    return render(request, 'videos35.html')

#Página dos slides NR01
def slides01(request):
    return render(request, 'slides01.html')

#Página dos slides NR06
def slides06(request):
    return render(request, 'slides06.html')

#Página dos slides NR12
def slides12(request):
    return render(request, 'slides12.html')

#Página dos slides NR17
def slides17(request):
    return render(request, 'slides17.html')

#Página dos slides NR18 andaimes
def slides18andaimes(request):
    return render(request, 'slides18-andaimes.html')

#Página dos slides NR18
def slides18soldagem(request):
    return render(request, 'slides18-soldagem.html')

#Página dos slides NR20
def slides20(request):
    return render(request, 'slides20.html')

#Página dos slides NR33
def slides33(request):
    return render(request, 'slides33.html')

#Página dos slides NR34
def slides34(request):
    return render(request, 'slides34.html')

#Página dos slides NR35
def slides35(request):
    return render(request, 'slides35.html')

#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/')
