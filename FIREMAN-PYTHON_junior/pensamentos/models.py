from django.db import models

class Pensador(models.Model):
    
    autor = models.CharField(max_length=100)
    fala = models.CharField(max_length=2000)

  
    def __str__(self):
        return self.autor