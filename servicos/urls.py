from django.urls import path
from clinica import views

urlpatterns = [
     path('medicos/', views.listar_medicos, name='ListarMedico'),
     path('consultas/nova/',views.criar_consultas, name='consultas'),
     path('consultas/<int:id>/', views.detalhes_consulta, name='detalhes')
]