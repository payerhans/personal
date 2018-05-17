from django.db import models

# Create your models here.
class Person(models.Model):
    pers_nr = models.CharField('Personalnummer', max_length=15, primary_key=True)
    vor_name = models.CharField('Vorname', max_length=30)
    nach_name = models.CharField('Nachname', max_length=30)
    title_pre = models.CharField(max_length=10, blank=True, null=True)
    title_past = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return "PersNr: {}, Name: {}".format(self.pers_nr, self.nach_name)