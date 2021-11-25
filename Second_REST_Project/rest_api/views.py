from django.shortcuts import render
from rest_framework.views import APIView
from . models import Student
from . serializers import StudentSerializer
from rest_framework.views import Response


class StudentList(APIView):
    def get(self, request):
        # students = Student.objects.get(first_name="Sireen")
        students = Student.objects.all()
        print(students)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


# Create your views here.
