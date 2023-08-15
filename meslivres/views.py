from django.shortcuts import render, redirect
from .models import Auteur, Livre
from .forms import LivreForm
from .forms import AuteurForm
from django.shortcuts import get_object_or_404
from django.db.models import Q




def home(request):
    return render(request, 'home.html')

#fonctionnalités pour ajouter des livres avec une redirection vers la page home
def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            livre = form.save()
            return redirect('home')
    else:
        form = LivreForm()

    return render(request, 'ajouter_livre.html', {'form': form})

#Meme fonctionnalités que pour ajouté un livre mais pour ajouter un auteurd depuis la page ajouter_livre
def ajouter_auteur(request):
    if request.method == 'POST':
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajouter_livre')
    else:
        form = AuteurForm()
    return render(request, 'ajouter_auteur.html', {'form': form})

#fonctionnalités de la page home pour afficher les auteurs et les livres, avec l'integration de la recherche 
def home(request):
    query = request.GET.get('q')
    livres = Livre.objects.all()
    auteurs = Auteur.objects.all()

    if query:
        livres = livres.filter(Q(titre__icontains=query) | Q(auteurs__nom__icontains=query))
        auteurs = auteurs.filter(Q(nom__icontains=query) | Q(prenom__icontains=query))

    return render(request, 'home.html', {'livres': livres, 'auteurs': auteurs, 'query': query})

#fonctionnalité du bouton supprimer pour supprimé un livre
def supprimer_livre(request, livre_id):
    livre = Livre.objects.get(pk=livre_id)
    livre.delete()
    return redirect('home')

#fonctionnalité pour editer un livre déjà existant
def editer_livre(request, livre_id):
    livre = Livre.objects.get(pk=livre_id)
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivreForm(instance=livre)

    return render(request, 'ajouter_livre.html', {'form': form})

#fiche de l'auteur pour récupérer les livres de l'auteur ainsi que ses données 
def fiche_auteur(request, auteur_id):
    auteur = get_object_or_404(Auteur, pk=auteur_id)
    livres = auteur.livre_set.all().order_by('-date_parution')
    
    context = {
        'auteur': auteur,
        'livres': livres
    }
    return render(request, 'fiche_auteur.html', context)