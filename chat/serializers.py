from rest_framework import serializers
from . import models

class PdfSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SavePdf
        fields=['pdf']