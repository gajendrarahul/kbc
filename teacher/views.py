from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,ListView,DetailView
from django .views import View

# Create your views here.
class TeacherHomeView(TemplateView):
    template_name = 'teacher/teacherhomepage.html'