from rest_framework import serializers
from . import models

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = "__all__"