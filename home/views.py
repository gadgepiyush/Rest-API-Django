from functools import partial
import imp
from urllib import request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
    

class StudentAPI(APIView):
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({
            'status':200,
            'payload': serializer.data
        })

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'status' : 403,
                'message' : serializer.errors
            })

        serializer.save()
        return Response({
            'status' : 200,
            'payload' : serializer.data,
            'message' : 'data sucessfully sent'
        })

    def put(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data)

            if not serializer.is_valid():
                return Response({
                        'status': 403,
                        'message' : serializer.errors
                    })

            serializer.save()

            return Response({
                'status' : 200,
                'payload' : serializer.data,
                'message': 'data sent succesfully'
            })

        except Exception as e:
            return Response({
                'status': 403,
                'message' : 'invalid id entered'
            })


    def patch(self, request):
        try:
            student_obj = Student.objects.get(id= request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'status' : 403,
                    'message' : 'invalid id entered'
                })

            serializer.save()
            return Response({
                'status' : 200,
                'payload' : serializer.data,
                'message' : 'data updated sucessfully'
            })

        except Exception as e:
            return Response({
                'status' : 403,
                'message' : "Exception ala."
            })

    def delete(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            student_obj.delete()

            return Response({
                'status' : 200,
                'message' : 'user deleted sucessfully'
            })

        except Exception as e:
            return Response({
                'status' : 403,
                'message': 'invalid id'
            })



'''
#API's build by not using APIview


@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)
    return Response({
        'status':200,
        'payload': serializer.data
    })


@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({
            'status': 403,
            'message' : serializer.errors
        })

    serializer.save()

    return Response({
        'status' : 200,
        'payload' : serializer.data,
        'message': 'data sent succesfully'
    })


@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)

        serializer = StudentSerializer(student_obj, data=request.data, partial=True)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({
                    'status': 403,
                    'message' : serializer.errors
                })

        serializer.save()

        return Response({
            'status' : 200,
            'payload' : serializer.data,
            'message': 'data sent succesfully'
        })

    except Exception as e:
        return Response({
            'status': 403,
            'message' : 'invalid id entered'
        })


@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()

        return Response({
            'status' : 200,
            'message' : 'user deleted sucessfully'
        })

    except Exception as e:
        return Response({
            'status' : 403,
            'message': 'invalid id'
        })



@api_view(['GET'])
def get_books(request):
    book_objs = Book.objects.all()
    serializer = BookSerilizer(book_objs, many=True)
    return Response({
        'status': 200,
        'payload': serializer.data
    })



@api_view(['POST'])
def post_book(requst):
    serializer = BookSerilizer(data=requst.data)
    if not serializer.is_valid():
        return Response({
            'status': 403,
            'message' : serializer.errors
        })

    serializer.save()

    return Response({
        'status' : 200,
        'payload' : serializer.data,
        'message' : 'data sent sucessfully'
    })


@api_view(['GET'])
def get_category(request):
    cat_obj = Category.objects.all()
    serializer = CategorySerilizer(cat_obj, many=True)

    return Response({
        'status' : 200,
        'payload' : serializer.data
    })


@api_view(['POST'])
def post_category(request):
    serializer = CategorySerilizer(data=request.data)
    if not serializer.is_valid():
        return Response({
            'status' : 403,
            'message' : serializer.errors
        })

    serializer.save()

    return Response({
        'status' : 200,
        'payload' : serializer.data,
        'message' : 'data sent sucessfully'
    })

'''