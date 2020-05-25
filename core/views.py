from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request, usuario)
        else:
            messages.error(request, "Usuário ou senha inválidos!")

    return redirect('/')


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    # pra um apenas ou select usuario
    # evento = Evento.objects.get(id=1)
    # para listar todos
    # evento = Evento.objects.all()

    usuario = request.user
    # quero permitir que mesmo com uma hora de ateaso ainda mosntre
    # entao pego hora atual menos 1
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados={}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)


@login_required(login_url='/login/')
def evento_submit(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        id_evento = request.POST.get('id_evento')
        usuario = request.user
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo,
                evento.data_evento = data_evento,
                evento.descricao = descricao,
                evento.usuario = usuario
                evento.save()
        else:
            Evento.objects.create(
                titulo=titulo,
                data_evento=data_evento,
                descricao=descricao,
                usuario=usuario
            )

    return redirect('/')


@login_required(login_url='/login/')
def evento_delete(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()

    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')


@login_required(login_url='/login/')
def json_lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')

    return JsonResponse(list(evento), safe=False)


# caso queira passar para alguma api externa e nao precise de login
# e se deseje ainda filtrar por usuario usar o metodo abaixo
def json_lista_evento_api(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)

