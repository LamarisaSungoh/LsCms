from django.shortcuts import render
from . import serializer
from . import models
from rest_framework import generics



# Create your views here.
    
class IntructorList(generics.ListCreateAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = serializer.InstructorSerializer

class InstructorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Instructor.objects.all()
    serializer_class = serializer.InstructorSerializer

# for student
class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer

class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer

# for Category Serializer
class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer

# Views for Course Model
class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializer.CourseSerializer

class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializer.CourseSerializer

# Views for Enrosllments Model
class EnrollmentList(generics.ListCreateAPIView):
    queryset = models.Enrollments.objects.all()
    serializer_class = serializer.EnrollmentSerializer

class EnrollmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Enrollments.objects.all()
    serializer_class = serializer.EnrollmentSerializer

# Views for Syllabus
class SyllabusList(generics.ListCreateAPIView):
    queryset = models.Syllabus.objects.all()
    serializer_class = serializer.SyllabusSerializer

class SyllabusDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Syllabus.objects.all()
    serializer_class = serializer.SyllabusSerializer

# Views for Content
class ContentList(generics.ListCreateAPIView):
    queryset = models.Content.objects.all()
    serializer_class = serializer.ContentSerializer

class ContentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Content.objects.all()
    serializer_class = serializer.ContentSerializer

# Views for Materials
class MaterialList(generics.ListCreateAPIView):
    queryset = models.Material.objects.all()
    serializer_class = serializer.MaterialSerializer

class MaterialDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Material.objects.all()
    serializer_class = serializer.MaterialSerializer

# Views for Faq
class FaqList(generics.ListCreateAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializer.FaqSerialzer

class FaqDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializer.FaqSerialzer

# Views for ClassSchedule
class ClassScheduleList(generics.ListCreateAPIView):
    queryset = models.ClassSchedule.objects.all()
    serializer_class = serializer.ClassScheduleSerializer

class ClassScheduleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClassSchedule.objects.all()
    serializer_class = serializer.ClassScheduleSerializer

# Views for QuizQAndA
class QuizQAndAList(generics.ListCreateAPIView):
    queryset = models.QuizQAndA.objects.all()
    serializer_class = serializer.QuizQAndASerializer

class QuizQAndADetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QuizQAndA.objects.all()
    serializer_class = serializer.QuizQAndASerializer

# Views for QuizQAndA
class QuizesList(generics.ListCreateAPIView):
    queryset = models.Quizes.objects.all()
    serializer_class = serializer.QuizesSerializer

class QuizesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quizes.objects.all()
    serializer_class = serializer.QuizesSerializer