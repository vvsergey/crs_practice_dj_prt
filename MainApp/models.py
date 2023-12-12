from django.db import models
# Create your models here.
class Translate(models.Model):
    article = models.TextField()

class Summary(models.Model):
    translate_text = models.TextField()

