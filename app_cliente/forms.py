# app_cliente/forms.py
from django import forms
from .models import Cliente, Sucursales

class IdLabelModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # muestra el id como etiqueta visible en el <select>
        return str(obj.pk)

class ClienteForm(forms.ModelForm):
    id_sucursal = IdLabelModelChoiceField(
        queryset=Sucursales.objects.all(),
        label='Sucursal (id)',
        required=False  # igual que en tu modelo (null=True, blank=True)
    )

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'edad', 'direccion', 'telefono', 'id_sucursal', 'foto_cliente']
