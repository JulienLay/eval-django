from django.db import models

class Analyste(models.Model):
    id_analyste = models.PositiveIntegerField()
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return f"Analyste {self.id}"

class Expert(models.Model):
    id_expert = models.PositiveIntegerField()
    analyste = models.ForeignKey(Analyste, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    def __str__(self):
        return f"Expert {self.id}"

class Capture(models.Model):
    analyst = models.ForeignKey(Analyste, on_delete=models.CASCADE)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    statut = models.CharField(max_length=100, default='En cours d\'enregistrement')
    interface_de_capture = models.CharField(max_length=100)
    nb_paquets_a_capturer = models.PositiveIntegerField()
    filtres = models.CharField(max_length=200)
    ETAT_CHOICES = (
        ('En attente', 'En attente'),
        ('Acceptée', 'Acceptée'),
        ('Refusée', 'Refusée'),
    )
    etat_demande = models.CharField(max_length=100, choices=ETAT_CHOICES)
    date_demande = models.DateField()
    heure_debut_captures = models.TimeField()
    heure_fin_captures = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return (
            f"Capture {self.id}\n"
            f"Statut : {self.statut}\n"
            f"Interface de capture : {self.interface_de_capture}\n"
            f"Nombre de paquets à capturer : {self.nb_paquets_a_capturer}\n"
            f"Filtres : {self.filtres}\n"
            f"Etat de la demande : {self.etat_demande}\n"
            f"Date de la demande : {self.date_demande}\n"
            f"Heure de début des captures : {self.heure_debut_captures}\n"
            f"Heure de fin des captures : {self.heure_fin_captures}\n"
            f"Description : {self.description}"
        )

class Demande(models.Model):
    interface_de_capture = models.CharField(max_length=100)
    nb_paquets_a_capturer = models.PositiveIntegerField()
    filtres = models.CharField(max_length=200)
    analyste = models.ForeignKey(Analyste, on_delete=models.CASCADE)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    ETAT_CHOICES = (
        ('En attente', 'En attente'),
        ('Acceptée', 'Acceptée'),
        ('Refusée', 'Refusée'),
    )
    etat_demande = models.CharField(max_length=100, choices=ETAT_CHOICES)

    def __str__(self):
        return f"Demande de {self.analyste.login} - {self.etat_demande}"
