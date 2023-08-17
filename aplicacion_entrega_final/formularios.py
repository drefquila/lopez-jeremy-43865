from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class registrousuario(UserCreationForm):
    email=forms.EmailField(label='email')
    password1=forms.CharField(label='contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contraseña',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields}

class Editarperfil(UserCreationForm):
    email=forms.EmailField(label='email')
    password1=forms.CharField(label='contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contraseña',widget=forms.PasswordInput)
    first_name=forms.CharField(label='nombre',max_length=20,required=False)
    last_name=forms.CharField(label='apellido',max_length=20,required=False)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        help_texts={k:'' for k in fields}

class Avatarform(forms.Form):
    imagen=forms.ImageField(required=True)