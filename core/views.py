from django.shortcuts import render
from core.models import Evento


def lista_eventos(request):
    # pra um apenas ou select usuario
    # evento = Evento.objects.get(id=1)
    # para listar todos
    # evento = Evento.objects.all()

    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
