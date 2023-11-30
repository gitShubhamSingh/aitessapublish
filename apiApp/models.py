from django.db import models


class Contact(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    companyName = models.CharField(max_length=200)
    additionalDetails = models.TextField()
