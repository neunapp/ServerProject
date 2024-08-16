from django.db import models

# Create your models here.
class Home(models.Model):

    name = models.CharField('name', max_length=50)
    msj = models.CharField('mensaje', max_length=50)
    

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Homes"

    def __str__(self):
        return self.name
