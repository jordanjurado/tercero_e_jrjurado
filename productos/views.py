from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from productos.models import Producto

def mostrarIndex(request):
    return render(request, 'index.html')


def mostrarListado(request):
    pro = Producto.objects.all().values()
    datos = { 'pro' : pro }
    return render(request, 'listado.html', datos)

@login_required
def index(request):
    return render(request,'index.html')
def mostrarFormRegistrar(request):
    return render(request, 'form_registrar.html')


def mostrarFormActualizar(request, id):
    try:
        pro = Producto.objects.get(id = id)
        datos = { 'pro' : pro }
        return render(request, 'form_actualizar.html', datos)
    except:
        pro = Producto.objects.all().values()
        datos = { 
            'pro' : pro, 
            'r2' : 'El ID ('+str(id)+') No Existe. Imposible Actualizar!!' 
        }
        return render(request, 'listado.html', datos)


def insertarProducto(request):
    if request.method == 'POST':
        nom = request.POST['txtnom']
        mar = request.POST['cbomar']
        pre = request.POST['txtpre']
        pro = Producto(nombre=nom, marca=mar, precio=pre)
        pro.save()
        datos = { 'r' : 'Registro Realizado Correctamente!!' }
        return render(request, 'form_registrar.html', datos)
    else:
        datos = { 'r2' : 'No Se Puede Procesar Solicitud!!' }
        return render(request, 'form_registrar.html', datos)



def actualizarProducto(request, id):
    if request.method == 'POST':
        nom = request.POST['txtnom']
        mar = request.POST['cbomar']
        pre = request.POST['txtpre']
        pro = Producto.objects.get(id = id)
        pro.nombre = nom
        pro.marca = mar
        pro.precio = pre
        pro.save()
        pro = Producto.objects.all().values()
        datos = { 
            'pro' : pro,
            'r' : 'Datos Modificados Correctamente!!' 
        }
        return render(request, 'listado.html', datos)
    else:
        datos = { 'r2' : 'No Se Puede Procesar Solicitud!!' }
        return render(request, 'listado.html', datos)


def eliminarProducto(request, id):
    try:
        pro = Producto.objects.get(id = id)
        pro.delete()
        pro = Producto.objects.all().values()
        datos = {
            'pro' : pro,
            'r' : 'Registro Eliminado Correctamente'
        }
        return render(request, 'listado.html', datos)
    except:
        pro = Producto.objects.all().values()
        datos = {
            'pro' : pro,
            'r2' : 'El ID ('+str(id)+') No Existe. Imposible Eliminar!!'
        }
        return render(request, 'listado.html', datos)