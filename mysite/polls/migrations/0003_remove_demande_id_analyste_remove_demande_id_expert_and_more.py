# Generated by Django 4.2 on 2023-08-09 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_analyste_capture_demande_expert_delete_choice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande',
            name='id_analyste',
        ),
        migrations.RemoveField(
            model_name='demande',
            name='id_expert',
        ),
        migrations.AddField(
            model_name='analyste',
            name='id_analyste',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capture',
            name='statut',
            field=models.CharField(default="En cours d'enregistrement", max_length=100),
        ),
        migrations.AddField(
            model_name='demande',
            name='analyste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.analyste'),
        ),
        migrations.AddField(
            model_name='expert',
            name='id_expert',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='demande',
            name='etat_demande',
            field=models.CharField(default='En attente', max_length=100),
        ),
    ]
