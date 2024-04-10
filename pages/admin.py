from django.contrib import admin
from .models import Cours,Exercice,Probleme,CNC , Eleve, Contact
# Register your models here.
admin.site.register(Eleve)
admin.site.register(Cours)
admin.site.register(Exercice)
admin.site.register(CNC)
admin.site.register(Probleme)

admin.site.register(Contact)