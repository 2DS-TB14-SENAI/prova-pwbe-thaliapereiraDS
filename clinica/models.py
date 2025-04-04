from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=30)
    crn = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome 

class Consulta(models.Model):
    paciente = models.CharField(max_length=50)  
    data = models.DateTimeField()  
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    cargo = [
        ("agenda", "agendado"),
        ("realiza", "realizado"),
        ("cancela", "cancelado"),
    ]
    
    status = models.CharField(max_length=20, choices=cargo)
