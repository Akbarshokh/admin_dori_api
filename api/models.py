from tabnanny import verbose
from django.db import models
from django.forms import CharField

class Dori(models.Model):
    nomi = models.CharField(max_length=255)
    rasmi = models.ImageField(upload_to="media", verbose_name="Dori Rasmlari", blank=True)
    tarkibi = models.TextField()
    qollanilishi = models.TextField()
    foydalanish_tartibi = models.TextField()
    is_active = models.BooleanField(verbose_name="Is Active?", default=True)

    class Meta:
        verbose_name = 'Dori'
        verbose_name_plural = 'Dori'

    def __str__(self):
        return self.nomi
    
        