from django.urls import path
from teacher import views
urlpatterns = [
    path('',views.TeacherHomeView.as_view(),name='teacherhomepage')
]