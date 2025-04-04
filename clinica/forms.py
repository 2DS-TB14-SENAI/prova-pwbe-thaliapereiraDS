from django import forms
from .models import Medico
from .models import Consulta


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'