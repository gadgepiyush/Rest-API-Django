from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('student', views.StudentAPI.as_view())
]


"""
    #paths without API view

    path('', views.home),
    path('postname', views.post_student),
    path('updatestudent/<id>/', views.update_student),
    path('deletestudent/<id>/', views.delete_student),
    path('getbook', views.get_books),
    path('postbook', views.post_book),
    path('getcategory', views.get_category),
    path('postcategory', views.post_category)
"""