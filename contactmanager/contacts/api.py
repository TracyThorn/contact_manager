from .models import Contact
from .serializers import ContactSerializer
from rest_framework import viewsets, permissions

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializer