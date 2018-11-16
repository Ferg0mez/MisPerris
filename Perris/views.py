from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from .forms import AgregarUsuario, Login, Mascotas
from .models import Usuario, Mascota
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView

#defino acciones posibles para establecer permisos
acciones=[
   {'Mostrar':'Home','url':'inicio'}
]
# Vista de index
def index(request):
    return render(request, "index.html")

# Vista de salida
def salir(request):
    logout(request)
    return redirect('/')

# Vista de login, el cual pide nombre de usuario, correo y contraseña para su creación
@login_required(login_url='login')
def gestionarUsuarios(request):
    actual=request.user
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
       # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        regDB=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        usuario=Usuario(user=regDB,perfil=data.get("perfil"))
        regDB.save()
        usuario.save()
    usuarios=Usuario.objects.all()
    form=AgregarUsuario()
    return render(request,"GestionarUsuarios.html",{'actual':actual,'form':form,'usuarios':usuarios,'acciones':acciones,})

def registro(request):
    actual=request.user
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
       # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        regDB=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        usuario=Usuario(user=regDB,perfil=data.get("perfil"))
        regDB.save()
        usuario.save()
    usuarios=Usuario.objects.all()
    form=AgregarUsuario()
    return render(request,"Registro.html",{'actual':actual,'form':form,'usuarios':usuarios,'acciones':acciones,})    

# Vista de ingreso del usuario
def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('listaMascota')
    return render(request,"login.html",{'form':form,})

# Vista de creación de la mascota 
@login_required(login_url='login')
def MascotaView(request):
    actual=request.user
    form = Mascotas(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listaMascota')
    form = Mascotas()
    return render (request,'GestionarMascotas.html',{'actual':actual,'form':form})

# Vista de listar las mascotas
@login_required(login_url='login')
def listaMascota(request):
    actual=request.user
    #mascota= Mascota.objects.all()
    mascota= Mascota.objects.get(estado='Disponible')
    contexto = {'actual':actual,'mascotas':mascota}
    return render(request,'listaMascota.html',contexto)

# Vista de editar mascotas
@login_required(login_url='login')
def editarMascota(request,idmascota):
    mascota = Mascota.objects.get(idmascota=idmascota)
    if request.method == 'GET':
        form = Mascotas(instance=mascota)
    else:
        actual=request.user
        form = Mascotas(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('listaMascota')
    return render (request, 'EditarMascotas.html',{'form':form})

# Vista de eliminar mascotas
@login_required(login_url='login')
def eliminarMascota (request,idmascota):
    actual=request.user
    mascota = Mascota.objects.get(idmascotaa=idmascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('listaMascota')
    return render(request, 'EliminarMascota.html', {'mascota':mascota})

# Vista de cambiar contraseña
@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Tu contraseña ha sido cambiada correctamente!')
            return redirect('login')
        else:
            messages.error(request, 'Porfavor arregla el error.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

# Clases necesarias para la construcción de las vistas de las mascotas

class MascotaList(ListView):
	model = Mascota
	template_name = 'listaMascota.html'
	paginate_by = 3

class MascotaCreate(CreateView):
	model = Mascota
	form_class = Mascotas
	template_name = 'GestionarMascotas.html'
	success_url = reverse_lazy('listaMascota')


class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = Mascotas
	template_name = 'EditarMascotas.html'
	success_url = reverse_lazy('listaMascota')


class MascotaDelete(DeleteView):
	model = Mascota
	template_name = 'EliminarMascota.html'
	success_url = reverse_lazy('listaMascota')

