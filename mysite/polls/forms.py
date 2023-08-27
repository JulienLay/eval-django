from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Demande, Capture

class AnalysteForm(UserCreationForm):
    id_analyste = forms.IntegerField(label="ID Analyste")
    role = forms.CharField(max_length=100)
    department = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'id_analyste', 'role', 'department')

class ExpertForm(UserCreationForm):
    id_expert = forms.IntegerField(label="ID Expert")
    analyste = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=False), label="Analyste")
    speciality = forms.CharField(max_length=100)
    experience_years = forms.IntegerField(label="Années d'expérience")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'id_expert', 'analyste', 'speciality', 'experience_years')

class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = (
            'interface_de_capture',
            'nb_paquets_a_capturer',
            'filtres',
            'analyste',
            'expert',
            'etat_demande',
        )

class CaptureForm(forms.ModelForm):
    class Meta:
        model = Capture
        fields = [
            'analyst',
            'expert',
            'statut',
            'nb_paquets_a_capturer',
            'filtres',
            'etat_demande',
            'date_demande',
            'heure_debut_captures',
            'heure_fin_captures',
            'description',
        ]