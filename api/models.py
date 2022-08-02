from distutils.command.upload import upload
from operator import truediv
from pyexpat import model
import re
from tabnanny import verbose
from django.db import models
from django.forms import CharField
from django.template.defaultfilters import slugify

#linklar - email, pnone, links

class Dori(models.Model):
    nomi = models.CharField(max_length=255)
    rasmi = models.ImageField(upload_to="images/", verbose_name="Dori Rasmlari", blank=True)
    tarkibi = models.TextField()
    qollanilishi = models.TextField()
    foydalanish_tartibi = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Dori'
        verbose_name_plural = 'Dori'

    def __str__(self):
        return self.nomi
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.nomi)
        return super().save(*args, **kwargs)
       
        
class Yangiliklar(models.Model):
    rasmi = models.ImageField(upload_to="yangiliklar/", verbose_name="Yangiliklar", blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Yangiliklar'
        verbose_name_plural = 'Yangiliklar'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    

class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    about = models.TextField()
    email = models.EmailField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    avatar = models.ImageField(upload_to = 'staff/')
    
    def __str__(self):
        return self.first_name

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.first_name

class Map(models.Model):
    map = CharField(max_length=255)

    def __str__(self):
        return self.map
    
class EmaiModel(models.Model):
    name = models.URLField()
    
    def __str__(self):
        return self.name
    
class TelefonModel(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class TwitterModel(models.Model):
    name = models.URLField()
    
    def __str__(self):
        return self.name
    
class FacebookModel(models.Model):
    name = models.URLField()
    
    def __str__(self):
        return self.name


class TelegramModel(models.Model):
    name = models.URLField()

    def __str__(self):
        return self.name

class InstagramModel(models.Model):
    name = models.URLField()

    def __str__(self):
        return self.name