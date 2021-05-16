from django.db import models
from Account.models import Account
from  phone_field import PhoneField

# Create your models here.
class TeacherDetails(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, blank=True, null=True)
    subject = models.CharField(max_length=100)
    started_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    end_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    salary = models.PositiveIntegerField()
    contact = PhoneField(blank=True, help_text='Contact number')
    address = models.CharField(max_length=200,null=True)
    slug = models.SlugField(max_length=50, unique=True,blank=True,null=True)
    user = models.OneToOneField(Account,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name