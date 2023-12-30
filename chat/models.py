from django.db import models

class SavePdf(models.Model):
    pdf = models.FileField()
