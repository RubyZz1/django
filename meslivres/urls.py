from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ajouter_livre/', views.ajouter_livre, name='ajouter_livre'),
    path('ajouter_auteur/', views.ajouter_auteur, name='ajouter_auteur'),
    
    #redirection qui utilise l'id pour ciblé le livre ou l'auteur pour ensuite afficher/editer des données en lien avec l'id 
    path('supprimer_livre/<int:livre_id>/', views.supprimer_livre, name='supprimer_livre'),
    path('editer_livre/<int:livre_id>/', views.editer_livre, name='editer_livre'),
    path('fiche_auteur/<int:auteur_id>/', views.fiche_auteur, name='fiche_auteur'),



]