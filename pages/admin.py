from django.contrib import admin
from .models import Cours,Exercice,DS,Probleme,DL , Eleve, Contact
# Register your models here.
admin.site.register(Eleve)
admin.site.register(Cours)
admin.site.register(Exercice)
admin.site.register(DS)
admin.site.register(Probleme)
admin.site.register(DL)
admin.site.register(Contact)