from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Paginas
from .models import Users, UserNueva
from .forms import PagsForm, UserForm
# Create your views here.

def inicio(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        password = request.POST['password']
        try:
            user = UserNueva.objects.get(rut=rut)
            pbasededatos=str(user.password)
            rbbdd =str(user.rol)
            if password == pbasededatos:
                if rbbdd == '1':
                    #login(request, user)
                    base = "base.html"
                    return redirect('index')
                else:
                    return redirect('index_copy')
            else:
                error_message = "Credenciales inválidas. Inténtalo de nuevo."
                return render(request, 'paginas/inicio.html', {'error_message': error_message})

        except UserNueva.DoesNotExist:
            error_message = "El usuario no existe. Inténtalo de nuevo."
            return render(request, 'paginas/inicio.html', {'error_message': error_message})

    else:  
        return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def nosotros_copy(request):
    return render(request, 'paginas/nosotros_copy.html')

def viewuser(request):
    return render(request, 'paginas/viewuser.html')

def index(request):
    pags = Paginas.objects.all()
    return render(request, 'paginas/index.html', {'pags': pags})

def index_copy(request):
    pags = Paginas.objects.all()
    return render(request, 'paginas/index_copy.html', {'pags': pags})

def editarp(request, id):
    pagina = Paginas.objects.get(id=id)
    formulario = PagsForm(request.POST, request.FILES or None, instance=pagina)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('dashboard')
    return render(request, 'pags/editar.html',{'formulario':formulario})

def eliminarp(request, id):
    pag = Paginas.objects.get(id=id)
    pag.delete()
    return redirect('dashboard')

def crearp(request):
    formulario = PagsForm(request.POST, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('dashboard')
    return render(request, 'pags/crear.html', 
    {'formulario':formulario})

def dashboard(request):
    pags = Paginas.objects.all()
    return render(request, 'paginas/dashboard.html', {'pags': pags})

def agregarp(request):
    return render(request, 'pags/agregar.html')

def editaru(request, id):
    user = UserNueva.objects.get(id=id)
    formulario = UserForm(request.POST, request.FILES or None, instance=user)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listar')
    return render(request, 'users/editar.html',{'formulario':formulario})

def agregaru(request):
    return render(request, 'users/crear.html')

def crearu(request):
    formulario = UserForm(request.POST, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listar')
    return render(request, 'users/crear.html', 
    {'formulario':formulario})

def listar(request):
    list1 = UserNueva.objects.all()
    print(list1)
    return render(request, 'users/listar.html', {'listar': list1})

def eliminaru(request, id):
    user = UserNueva.objects.get(id=id)
    user.delete()
    return redirect('listar')

def buscar(request):
    if 'termino_busqueda' in request.GET:
        termino = request.GET['termino_busqueda']
        resultados = Paginas.objects.filter(titulo=termino)
    else:
        resultados = None
    return render(request, 'buscar.html', {'resultados': resultados})