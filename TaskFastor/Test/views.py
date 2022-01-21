from. models import Employee,Teacher,Student
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Test.serializers import EmployeeSerializer,TeacherSerializer,StudentSerializer


class EmployeefoViewSet(viewsets.ModelViewSet):
    """
    API to fetch, update, delete and find all super -Admin record.
    Admin must be able to add/list every user in the database
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
   
class TeacherViewSet(viewsets.ModelViewSet):
    """
    API to and find all Teacher record. Teacher must be able to add/list the students.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API to Students must be able to see his  information only.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   
""" Now, we need to authenticate and obtain the token. which we will get at endpoint is 
   """
class HelloView(APIView):
    permission_classes = (IsAuthenticated, )

def get(self, request):
    content = {'message': 'Hello, sir'}
    return Response(content)