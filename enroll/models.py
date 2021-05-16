from django.db import models

# Create your models here.
class Enrolled(models.Model):
    faculty = models.CharField(max_length=100)
    end_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    batch = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.faculty
    
