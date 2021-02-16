from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        'Título',
        max_length=200
    )
    author = models.ForeignKey(
        'auth.User',
        verbose_name='Autor',
        on_delete=models.CASCADE,
    )
    body = models.TextField(
        verbose_name='Cuerpo'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

