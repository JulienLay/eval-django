from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),

    # Connexion
    path('authentification/', LoginView.as_view(template_name='polls/authentification.html'), name='authentification'),

   # Déconnexion
    #path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    #ANAYLYSTE
    path('demande_capture/', LoginView.as_view(template_name='polls/demande_capture.html'), name='demande_capture'),
    path('observer_capture/', views.observer_capture, name='observer_capture'),
    path('observe_capture/<int:capture_id>/', views.observe_capture, name='observe_capture'),

    # EXPERT
    path('expert/observer_capture/', views.expert_observer_capture, name='expert_observer_capture'),
    path('expert/observe_capture/<int:capture_id>/', views.expert_observe_capture, name='expert_observe_capture'),
    path('expert/delete_capture/<int:capture_id>/', views.expert_delete_capture, name='expert_delete_capture'),

    path('expert/demarrer_capture/', LoginView.as_view(template_name='polls/demarrer_capture.html'), name='demarrer_capture'),
    path('expert/enregistrer_capture/', LoginView.as_view(template_name='polls/enregistrer_capture.html'), name='enregistrer_capture'),
    path('expert/captures_courantes/', LoginView.as_view(template_name='polls/captures_courantes.html'), name='captures_courantes'),
]