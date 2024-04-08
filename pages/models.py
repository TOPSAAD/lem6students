from django.db import models




class Eleve(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="users/%y/%m/%d")

    def __str__(self):
        return self.username



class Cours(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="cours/%y/%m/%d")
    image2 = models.ImageField(upload_to="cours/%y/%m/%d")
    file = models.CharField(max_length=100,default='0')
    matiere = models.CharField(max_length=100,default='0')
    category = models.CharField(max_length=100)

    classe = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Exercice(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="exos/%y/%m/%d")
    image2 = models.ImageField(upload_to="exos/%y/%m/%d")
    file = models.CharField(max_length=100,default='0')
    matiere = models.CharField(max_length=100,default='0')
    category = models.CharField(max_length=100)

    classe = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class DS(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="ds/%y/%m/%d")
    image2 = models.ImageField(upload_to="ds/%y/%m/%d")
    file = models.CharField(max_length=100,default='0')
    matiere = models.CharField(max_length=100,default='0')
    category = models.CharField(max_length=100)

    classe = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Probleme(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="prob/%y/%m/%d")
    image2 = models.ImageField(upload_to="prob/%y/%m/%d")
    file = models.CharField(max_length=100,default='0')
    matiere = models.CharField(max_length=100,default='0')
    category = models.CharField(max_length=100)

    classe = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class DL(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to="dl/%y/%m/%d")
    image2 = models.ImageField(upload_to="dl/%y/%m/%d")
    file = models.CharField(max_length=100,default='0')
    matiere = models.CharField(max_length=100,default='0')
    category = models.CharField(max_length=100)

    classe = models.CharField(max_length=10)
    description = models.TextField()
    
    def __str__(self):
        return self.name

    

class Contact(models.Model):
    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    message = models.CharField(max_length=1010)
    

    def __str__(self):
        return self.nom
