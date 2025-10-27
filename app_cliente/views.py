from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Sucursales
from .forms import ClienteForm

def listar_clientes(request):
    clientes = Cliente.objects.select_related('id_sucursal').all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)  # ✅ request.FILES añadido
        if form.is_valid():
            form.save()
            return redirect('app:listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'formulario_cliente.html', {'form': form, 'titulo': 'Crear Cliente'})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)  # ✅ request.FILES añadido
        if form.is_valid():
            form.save()
            return redirect('app:detalle_cliente', cliente_id=cliente.id)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'formulario_cliente.html', {'form': form, 'titulo': 'Editar Cliente'})

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('app:listar_clientes')
    return render(request, 'confirmar_borrar_cliente.html', {'cliente': cliente})
