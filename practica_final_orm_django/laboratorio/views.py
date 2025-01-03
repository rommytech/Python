from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm

# Mostrar lista de laboratorios
def laboratorio_mostrar(request):
    laboratorios = Laboratorio.objects.all()
    
    # Incrementa el contador de visitas
    visitas = request.session.get('visitas', 0)
    request.session['visitas'] = visitas + 1

    return render(request, 'laboratorio/mostrar.html', {
        'laboratorios': laboratorios,
        'visitas': visitas + 1
    })


# Insertar (crear) nuevo laboratorio
def laboratorio_insertar(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_laboratorios')
    else:
        form = LaboratorioForm()
    
    return render(request, 'laboratorio/insertar.html', {'form': form})


# Editar (actualizar) laboratorio existente
def laboratorio_editar(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('mostrar_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    
    return render(request, 'laboratorio/editar.html', {'form': form})


# Eliminar laboratorio
def laboratorio_eliminar(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('mostrar_laboratorios')
    
    return render(request, 'laboratorio/eliminar.html', {'laboratorio': laboratorio})
