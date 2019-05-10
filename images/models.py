from django.db import models

# Create your models here.
class Images(models.Model):
    images=models.ImageField(upload_to='images')
    class Meta:
        verbose_name_plural='Картины'
        verbose_name='Картины'
