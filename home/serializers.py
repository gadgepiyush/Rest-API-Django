from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

        

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if data['age']<17:
            raise serializers.ValidationError({
                'error' : 'age cannot be less then 18'
            })

        #check for seeing name does not contain any digit
        if any(char.isdigit() for char in data['name']):
            raise serializers.ValidationError({
                'error' : 'name cannot contain digit'
            })

        return data


class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    
class BookSerilizer(serializers.ModelSerializer):
    category = CategorySerilizer()
    class Meta:
        model = Book
        fields = '__all__'