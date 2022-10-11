from dataclasses import field
from rest_framework import serializers
from .models import *

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