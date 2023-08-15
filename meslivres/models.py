from django.db import models

#création de la table auteur dans la BDD
class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    ddn = models.DateField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
#création de la table livre dans la BDD
class Livre(models.Model):
    titre = models.CharField(max_length=100)
    nombre_page = models.PositiveIntegerField()
    genres = models.CharField(max_length=100)
    date_parution = models.DateField()
    auteurs = models.ManyToManyField(Auteur)
    couverture = models.ImageField(upload_to='./images', blank=True, null=True)

    def __str__(self):
        return self.titre
    
    def date_parution_format_fr(self):
        return self.date_parution.strftime('%d/%m/%Y')
    

    


