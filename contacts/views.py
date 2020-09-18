from rest_framework import viewsets
from rest_framework.views import APIView
from contacts import models, serializers

from rest_framework.schemas.openapi import AutoSchema


class ContactViewset(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


# class MyView(APIView):
#     schema = AutoSchema(operation_id_base="Custom")
