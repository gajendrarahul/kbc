from django.db import models
from phone_field import PhoneField
from Account.models import Account

# Create your models here.
class StudentDetails(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200,null=True)
    rollno = models.PositiveIntegerField(default=None)
    contact = PhoneField(blank=True, help_text='Contact phone number')
    image = models.ImageField(upload_to='StudentImages',null=True,blank=True)
    slug = models.SlugField(max_length=50,default=None,unique=True)
    user = models.OneToOneField(Account,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name
    