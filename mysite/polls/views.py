from django.shortcuts import render, redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import DemandeForm, ExpertForm
from .models import Analyste, Capture
from scapy.all import *
from threading import Thread

def index(request):
    return render(request, 'polls/index.html')

@login_required
def redirect_after_login(request):
    return redirect('demande_capture')

def authentification(request):
    return LoginView.as_view(template_name='authentification.html')(request)

def s_authentifier(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Vérification des informations d'authentification
        analyste = Analyste.objects.filter(login=username, password=password).first()

        if analyste is not None:
            # Authentification réussie
            # Redirection vers la page de demande de capture spécifique
            return redirect('demande_capture')

        else:
            # Authentification échouée, afficher un message d'erreur
            return render(request, 'authentification.html', {'error_message': 'Identifiants invalides.'})

@login_required
def demander_capture(request):

    # Obtenir la liste des noms d'interfaces avec Scapy
    interfaces = get_if_list()

    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire et les enregistrer
            demande = form.save()
            return redirect('captures_en_attente')
    else:
        form = DemandeForm()

    context = {
        'form': form,
        'interfaces': interfaces,  # Ajouter la liste des interfaces
    }

    return render(request, 'demande_capture.html', context)



def create_expert(request):
    if request.method == 'POST':
        form = ExpertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expert_list')
    else:
        form = ExpertForm()

    return render(request, 'create_expert.html', {'form': form})

def captures_enregistrees(request):
    captures = Capture.objects.filter(expert=request.user)
    return render(request, 'captures_enregistrees.html', {'captures': captures})

@login_required
def enregistrer_capture(request):
    if request.method == 'POST':
        capture_id = request.POST.get('capture_id')
        try:
            capture = Capture.objects.get(pk=capture_id, expert=request.user)

            # Vérifier si la capture est en cours d'enregistrement
            if capture.statut == 'En cours d\'enregistrement':
                capture.statut = 'Enregistrée'
                capture.save()

                # Rediriger vers la page des captures courantes de l'expert
                return redirect('captures_courantes')
            else:
                # La capture n'est pas en cours d'enregistrement, afficher un message d'erreur.
                message = 'La capture sélectionnée ne peut pas être enregistrée car elle n\'est pas en cours d\'enregistrement.'
                return render(request, 'enregistrer_capture.html', {'captures': Capture.objects.filter(expert=request.user), 'message': message})

        except Capture.DoesNotExist:
            # La capture spécifiée n'existe pas ou n'appartient pas à l'expert connecté, afficher un message d'erreur.
            message = 'La capture spécifiée n\'existe pas ou n\'appartient pas à l\'expert connecté.'
            return render(request, 'enregistrer_capture.html', {'captures': Capture.objects.filter(expert=request.user), 'message': message})

    else:
        # Afficher la liste des captures courantes de l'expert
        captures = Capture.objects.filter(expert=request.user)
        return render(request, 'enregistrer_capture.html', {'captures': captures})

def observer_capture(request):
    captures = Capture.objects.all()  # Obtenir toutes les captures disponibles

    context = {
        'captures': captures
    }

    print("Captures in observer_capture view:", captures)

    return render(request, 'polls/observer_capture.html', context)

def observe_capture(request, capture_id):
    capture = Capture.objects.get(pk=capture_id)

    context = {
        'capture': capture
    }

    return render(request, 'polls/observe_capture.html', context)

def expert_observe_capture(request, capture_id):
    capture = get_object_or_404(Capture, pk=capture_id)

    if request.method == 'POST' and 'delete' in request.POST:
        capture.delete()
        return redirect('polls:expert_observer_capture')  # Redirige vers la liste des captures

    context = {'capture': capture}
    return render(request, 'polls/expert_observe_capture.html', context)

def expert_observer_capture(request):
    captures = Capture.objects.all()
    context = {'captures': captures}
    return render(request, 'polls/expert_observer_capture.html', context)

def expert_delete_capture(request, capture_id):
    capture = get_object_or_404(Capture, pk=capture_id)

    if request.method == 'POST':
        capture.delete()
        return redirect('polls:expert_observer_capture')  # Redirige vers la liste des captures

    context = {'capture': capture}
    return render(request, 'polls/expert_delete_capture.html', context)

# Variable pour suivre l'état de la capture
capture_started = False

def demarrer_capture(request):
    global capture_started

    if request.method == 'POST':
        if not capture_started:
            capture_started = True
            start_capture_thread()

    context = {
        'capture_started': capture_started,
    }

    return render(request, 'demarrer_capture.html', context)

def start_capture_thread():
    capture_thread = Thread(target=capture_packets)
    capture_thread.start()

def capture_packets():
    global capture_started

    interface = "enp0s3"

    # Démarrer la capture
    packets = sniff(iface=interface, count=10)  # Capturer 10 paquets

    # Traiter les paquets capturés
    captured_packets = [str(packet) for packet in packets]

    capture_started = False