from django.contrib import admin
from .models import Book, Category, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Category)