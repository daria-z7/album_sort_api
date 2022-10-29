from django.db import models


class Artist(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=200,
    )

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=200,
    )
    artist = models.ForeignKey(
        Artist,
        verbose_name='Album author',
        on_delete=models.CASCADE,
        related_name='albums',
    )
    year = models.IntegerField(
        verbose_name='Year',
    )

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'artist'],
                name='unique_name_artist'
            )
        ]

    def __str__(self):
        return f'{self.name}[{self.year}]'


class Track(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=200,
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='tracks'
    )

    def __str__(self):
        return self.name
