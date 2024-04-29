from datetime import datetime

from authentication.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'birthdate', 'can_be_contacted', 'can_data_be_shared']
        
    def create(self, validated_data):
        today = datetime.today()
        birthdate = validated_data['birthdate']
        age = (today.year - birthdate.year) - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if age < 15:
            raise serializers.ValidationError("User must be at least 15 years old.")
        
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)