from django.db import models

# Create your models here.


class Freelancer(models.Model):
    Name=models.CharField(max_length=50,default='Enter your name')
    Address=models.CharField(max_length=50,default='Enter your Address')
    Phone=models.IntegerField(default='Enter your Number')
    Email=models.EmailField(default='Enter your email')
    Description=models.TextField(default='Write your self')



    def __self__(self):
        return f'My name is {self.Name}. I am from {self.Address}. my phone number and email are {self.Phone} and {self.Email}. {self.Description}'
        





  
    
