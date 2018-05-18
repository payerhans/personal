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

class ZeitKorrektur(models.Model):
    KORR_TYPES = (
        ('DI', 'Dienst'),
        ('SU', 'Sonderurlaub'),
        ('VB', 'Vergessene Buchung'),
        ('DR', 'Dienstreise'),
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    art = models.CharField(max_length=2, choices=KORR_TYPES)
    datum = models.DateField()
    beginn = models.TimeField()
    ende = models.TimeField()
    begruendung = models.TextField('Begründung', max_length=150)
    gedruckt = models.BooleanField()

    def __str__(self):
        return "{}, {}".format(self.art, self.datum)