from django.db import models

# Create your models here.
class Festival(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.nome