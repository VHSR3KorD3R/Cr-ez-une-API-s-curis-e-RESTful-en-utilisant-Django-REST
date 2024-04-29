from django.shortcuts import render
from authentication.models import User
from rest_framework import viewsets
from authentication.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    
    
    def get_queryset(self):
        # # if self.request.user.is_superuser:
        return User.objects.all()