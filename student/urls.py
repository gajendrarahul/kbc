from django.urls import path
from student import views
urlpatterns = [
    path('',views.StudentHomeView.as_view(),name='studenthome')
]
