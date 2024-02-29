from django.urls import path
from student.views import * 
urlpatterns=[
    path("",home),
    path("about/",about),
    path("record/",record),
    path("registration/",registration),
    path('python/',python),
    path('java/',java),
    path('aws/',aws),
    path('update/<int:id>/',update),
    path('delete/<int:id>/',delete),
]