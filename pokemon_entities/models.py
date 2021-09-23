from django.db import models


class Pokemon (models.Model):
    title = models.CharField(max_length=200, blank=False, null = False,
                             verbose_name='имя')
    image = models.ImageField(upload_to='pokemons', blank=True,
                              verbose_name='картинка')
    title_en = models.CharField(max_length=200, blank=True,
                                verbose_name='имя на английском языке')
    title_jp = models.CharField(max_length=200, blank=True,
                                verbose_name='имя на японском языке')
    description = models.TextField(blank=True, verbose_name='описание')
    next_evolution = models.ForeignKey(
        'self',
        related_name='+',
        verbose_name='в кого эволюционирует',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    previous_evolution = models.ForeignKey(
        'self',
        related_name='+',
        verbose_name='из кого эволюционировал',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity (models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='pokemon_entities',
                                verbose_name='покемон',
                                on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='долгота')
    lon = models.FloatField(verbose_name='широта')
    appeared_at = models.DateTimeField(blank=True, null=True,
                                       verbose_name='появился в')
    disappeared_at = models.DateTimeField(blank=True, null=True,
                                          verbose_name='исчез в')
    level = models.IntegerField(verbose_name='уровень')
    health = models.IntegerField(blank=True, null=True,
                                 verbose_name='здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='атака')
    defence = models.IntegerField(blank=True, null=True, verbose_name='защита')
    stamina = models.IntegerField(blank=True, null=True,
                                  verbose_name='выносливость')
