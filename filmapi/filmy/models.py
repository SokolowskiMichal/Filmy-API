from django.db import models

# Create your models here.
from django.db.models import IntegerField


class Film(models.Model):
    objects = None
    tytul = models.CharField(max_length=64)
    opis = models.TextField()
    rok: IntegerField = models.IntegerField(default=1900)
    plakat = models.ImageField(upload_to='plakaty', default=None)


    def __str__(self):
        return self.tytul
