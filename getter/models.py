from django.db import models

# Create your models here.
class url_inicial(models.Model):
    id_url_inicial = models.AutoField(primary_key=True)
    link = models.CharField(blank=True, null=True, max_length=255)

class urls_relacionadas(models.Model):
    id_urls_relacionadas = models.AutoField(primary_key=True)
    id_url_inicial = models.ForeignKey('url_inicial', on_delete=models.CASCADE)
    link = models.CharField(blank=True, null=True, max_length=255)