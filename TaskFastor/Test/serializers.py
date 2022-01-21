from . models import Employee,Teacher,Student
from rest_framework import serializers

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id","teacher_name","student_add","update_date","email_id"]

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ["id","student_name","course_name","class_name","email_id"]

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Employee
        fields = ["id","employee_name","user_add","email_id","password","teacher","student"]


