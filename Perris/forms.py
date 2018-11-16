from django import forms
from .models import Mascota

perfiles=(
    ('Usuario','Usuario'),
)

class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    perfil=forms.ChoiceField(choices=perfiles)


class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")

estados=(
    ('Rescatado','Rescatado'),
    ('Disponible','Disponible'),
    ('Adoptado','Adoptado'),
)

class Mascotas(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [
        'nomascota',
        'raza',
        'descripcion',
        'estado',
        'fotografia'
    ]

    labels = {
        'nombre':'Nombre Mascota',
        'raza':'Raza Mascota',
        'descripcion':'Descripcion',
        'estado' : 'Estado',
        'fotografia' : 'Foto'
    }
    estado=forms.ChoiceField(choices=estados, initial='Rescatado')
    widgets ={
        'nomascota': forms.TextInput(attrs={'class':'form=control'}),
        'raza': forms.TextInput(attrs={'class':'form=control'}),
        'descripcion': forms.TextInput(attrs={'class':'form=control'}),
        
    }