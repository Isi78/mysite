from django.db import models

class Artista(models.Model):
    artista = models.CharField(null=False, blank=False, max_length=100)

    class Meta:
        ordering = ['artista']

    def __str__(self):
        return '{} {}'.format(self.artista)

class Song(models.Model):
    titolo = models.CharField(null=False, blank=False, max_length=100)
    canzone = models.FileField(null=True, blank=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    class Meta:
        ordering = ['titolo']

    def __str__(self):
        return '{} {}'.format(self.titolo)



























# Create your models here.
