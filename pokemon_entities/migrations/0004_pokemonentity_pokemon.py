# Generated by Django 3.1.13 on 2021-09-17 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_pokemonentity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='pokemon_entities.pokemon'),
            preserve_default=False,
        ),
    ]
