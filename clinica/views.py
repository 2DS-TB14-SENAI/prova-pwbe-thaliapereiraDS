from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Consulta
from .forms import ConsultaForm

# Listar médicos
def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, "clinica/listar_medicos.html", {'medicos': medicos})

# Criar consultas
def criar_consultas(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')  # Aqui você precisa garantir que a URL 'consultas' esteja configurada no seu urls.py
    else:
        form = ConsultaForm()

    return render(request, 'clinica/criar_consultas.html', {'form': form})

# Detalhes da consulta
def detalhes_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    return render(request, 'clinica/detalhes_consulta.html', {'consulta': consulta})
