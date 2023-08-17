from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.views.generic import ListView,UpdateView,DeleteView,DetailView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .formularios import registrousuario,Editarperfil,Avatarform
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if avatares:
        url_avatar=avatares[0].imagen.url
    else:
        url_avatar=None    
    return render(request,'inicio.html')

#Peliculas_________________________________________________________________________________________

class listapeliculas(ListView):
    model=Peliculas
    template_name='peliculas/peliculas.html'

class añadirpelicula(LoginRequiredMixin,CreateView):
    model=Peliculas
    fields=['nombre','genero','fecha_de_estreno','taquilla','director','elenco','duracion','sinopsis','imagen']
    template_name='peliculas/añadirpelicula.html'
    success_url=reverse_lazy('peliculas')

class detallespeliculas(LoginRequiredMixin,DetailView):
    model=Peliculas
    template_name='peliculas/detallespelicula.html'

class eliminarpelicula(LoginRequiredMixin,DeleteView):
    model=Peliculas
    template_name='peliculas/eliminarpelicula.html'
    success_url=reverse_lazy('peliculas')

class editararpelicula(LoginRequiredMixin,UpdateView):
    model=Peliculas
    fields=['nombre','genero','fecha_de_estreno','taquilla','director','elenco','duracion','sinopsis','imagen']
    template_name='peliculas/editarpelicula.html'
    success_url=reverse_lazy('peliculas')

#series________________________________________________________________________________________

class listaseries(ListView):
    model=Series
    template_name='series/series.html'

class añadirserie(LoginRequiredMixin,CreateView):
    model=Series
    fields=['nombre','fecha_de_estreno','productor','elenco','temporadas','capitulos','genero','sinopsis','imagen']
    template_name='series/añadirserie.html'
    success_url=reverse_lazy('series')
       
class detallesserie(LoginRequiredMixin,DetailView):
    model=Series
    template_name='series/detallesseries.html'

class eliminarserie(LoginRequiredMixin,DeleteView):
    model=Series
    template_name='series/eliminarserie.html'
    success_url=reverse_lazy('series')

class editarserie(LoginRequiredMixin,UpdateView):
    model=Series
    fields=['nombre','fecha_de_estreno','productor','elenco','temporadas','capitulos','genero','sinopsis','imagen']
    template_name='series/editarserie.html'
    success_url=reverse_lazy('series')

#programas________________________________________________________________________________________

class listaprogramas(ListView):
    model=Programas
    template_name='programas/programas.html'

class añadirprograma(LoginRequiredMixin,CreateView):
    model=Programas
    fields=['nombre','fecha_de_emision','director','elenco','temporadas','capitulos','sinopsis','imagen']
    template_name='programas/añadirprograma.html'
    success_url=reverse_lazy('programas')

class detallesprograma(LoginRequiredMixin,DetailView):
    model=Programas
    template_name='programas/detallesprograma.html'

class eliminarprograma(LoginRequiredMixin,DeleteView):
    model=Programas
    template_name='programas/eliminarprograma.html'
    success_url=reverse_lazy('programas')

class editarprograma(LoginRequiredMixin,UpdateView):
    model=Programas
    fields=['nombre','fecha_de_emision','director','elenco','temporadas','capitulos','sinopsis','imagen']
    template_name='programas/editarprograma.html'
    success_url=reverse_lazy('programas')

#documentales____________________________________________________________________________________

class listadocumental(ListView):
    model=Documentales
    template_name='documentales/documentales.html'

class añadirdocumental(LoginRequiredMixin,CreateView):
    model=Documentales
    fields=['nombre','fecha_de_estreno','director','elenco','duracion','genero','sinopsis','imagen']
    template_name='documentales/añadirdocumental.html'
    success_url=reverse_lazy('documentales')

class detallesdocumental(LoginRequiredMixin,DetailView):
    model=Documentales
    template_name='documentales/detallesdocumental.html'

class eliminardocumental(LoginRequiredMixin,DeleteView):
    model=Documentales
    template_name='documentales/eliminardocumental.html'
    success_url=reverse_lazy('documentales')

class editardocumental(LoginRequiredMixin,UpdateView):
    model=Documentales
    fields=['nombre','fecha_de_estreno','director','elenco','duracion','genero','sinopsis','imagen']
    template_name='documentales/editardocumental.html'
    success_url=reverse_lazy('documentales')

#login,logout y registro__________________________________________________________

def logearse(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nusuario=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')
            usuario=authenticate(username=nusuario,password=clave)
            if usuario is not None:
                login(request,usuario)
                return render(request,'inicio.html')
        else:
            form=AuthenticationForm()
            return render(request,'logearse.html',{'form':form,'mensaje':'los datos ingresados no coinciden con ningun usuario'})    
    else:
        form=AuthenticationForm()
        return render(request,'logearse.html',{'form':form})

def registrarse(request):
    if request.method=='POST':
        form=registrousuario(request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            form.save()
            return render(request,'inicio.html',{'mensaje':'se ha registrado exitosamente'})
        else:
            return render(request,'registrarse.html',{'form':form,'mensaje':'los datos ingresados no son validos para el formulario de registro'})
    else:
        form=registrousuario()
        return render(request,'registrarse.html',{'form':form})

@login_required
def editarusuario(request):
    usuario = request.user

    if request.method == 'POST':
        form = Editarperfil(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('inicio')
        else:
            form = Editarperfil(instance=usuario)
            return render(request,'editar.perfil',{'form':form,'mensaje':'los datos ingresados no son validos'})
    else:
        form = Editarperfil(instance=usuario)

    return render(request, 'editarperfil.html', {'form': form})

@login_required
def asignaravatar(request):
    if request.method=='POST':
        form=Avatarform(request.POST,request.FILES)
        if form.is_valid():
            u=User.objects.get(username=request.user)
            avatarviejo=Avatar.objects.filter(user=u)
            if len(avatarviejo)>0:
                avatarviejo[0].delete()
            avatarnuevo=Avatar(user=u,imagen=form.cleaned_data['imagen'])
            avatarnuevo.save()
            imagen=Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar']=imagen
            return render(request,'inicio.html')
    else:
        form=Avatarform()
        return render(request,'asignaravatar.html',{'formulario':form})
           
def acercademi(request):
    return render(request,'acerca_de_mi.html')           