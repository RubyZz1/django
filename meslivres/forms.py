from django import forms
from .models import Livre
from .models import Auteur
from django_select2.forms import Select2MultipleWidget


class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = '__all__'

#formulaire de ajouter_livre avec l'utilisation de select2 pour la selection de l'auteur 
class LivreForm(forms.ModelForm):
    auteurs = forms.ModelMultipleChoiceField(
        queryset=Auteur.objects.all(),
        widget=Select2MultipleWidget  # Utiliser le widget Select2
    )

    
    class Meta:
        model = Livre
        fields = '__all__'

