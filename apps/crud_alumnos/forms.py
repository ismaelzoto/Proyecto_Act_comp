# aqui se Crea el formulario

from django import forms
from apps.crud_alumnos.models import alumnos,estado


class alumnosForm(forms.ModelForm):
    class Meta:
        model = alumnos
        fields = [
            'nocontrol',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'email',
            'telefono',
            'fecha_nacimiento',
            'sexo',
            'calle',
            'numero_exterior',
            'numero_interior',
            'colonia',
            'password',
            'estatus',
            'carrera',
            'localidad',
            'rol'
        ]
        labels = {
            'nocontrol':'Numero de Control',
            'nombre':'Nombres',
            'apellido_paterno':'Apellido Paterno',
            'apellido_materno':'Apellido Materno',
            'email':'Correo Electronico',
            'telefono':'Numero de Telefono',
            'fecha_nacimiento':'Fecha de Nacimiento',
            'sexo':'Sexo',
            'calle':'Direccion',
            'numero_exterior':'Numero Exterior',
            'numero_interior':'Numero Interior',
            'colonia':'Colonia',
            'password':'Contraseña',
            'estatus':'Estatus',
            'carrera':'Carrera',
            'localidad':'Localidad',
            'rol':'Rol'
        }

        widgets = {
            'nocontrol':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento':forms.TextInput(attrs={'class':'datepicker'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'calle':forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior':forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior':forms.TextInput(attrs={'class':'form-control'}),
            'colonia':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'estatus':forms.TextInput(attrs={'class':'form-control'}),
            'carrera':forms.Select(attrs={'class':'form-control'}),
            'localidad':forms.Select(attrs={'class':'form-control'}),
            'rol':forms.Select(attrs={'class':'form-control'})
        }

#aqui inicia el formulario de estado

class estadoForm(forms.ModelForm):
    class Meta:
        model = estado
        fields = [
            'id_estado',
            'nombre_estado'
            ]
        labels = {
            'id_estado':'Clave de Estado',
            'nombre_estado':'Nombre del Estado'
        }
        widgets = {
            'id_estado': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_estado': forms.TextInput(attrs={'class': 'form-control'}),
        }