from django.contrib import admin
from .models import Person, ZeitKorrektur

# Register your models here.
admin.site.register(Person)
admin.site.register(ZeitKorrektur)