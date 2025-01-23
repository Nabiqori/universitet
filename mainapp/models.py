from django.db import models
from django.db.models import SET_NULL


class Yonalish(models.Model):
    nom = models.CharField(max_length=100)
    aktiv = models.BooleanField()
    def __str__(self):
        return self.nom
class Fan(models.Model):
    nom = models.CharField(max_length=100)
    yonalish = models.ForeignKey(Yonalish, on_delete=SET_NULL, null=True, blank=True)
    asosiy = models.BooleanField()
    def __str__(self):
        return self.nom
class Ustoz(models.Model):
    nom = models.CharField(max_length=100)
    jins = models.CharField(max_length=100, choices=(('Erkak', 'Erkak'),("Ayol", "Ayol")))
    yosh = models.IntegerField()
    daraja = models.CharField(max_length=100 , choices=(("Bakalavr", "Bakalavr"),("Magistr","Magistr"),("Dotsent","Dotsent"),("Professor","Professor")))
    fan = models.ForeignKey(Fan,on_delete=SET_NULL,null=True, blank=True)
    def __str__(self):
        return self.nom
