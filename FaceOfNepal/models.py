from django.db import models

# Create your models here.
class Address(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Freelancer(models.Model):
    Name=models.CharField(max_length=50)
    Address=models.ForeignKey(Address,on_delete=models.CASCADE)
    Phone=models.IntegerField()
    Email=models.EmailField()
    describe=models.TextField(default='Write your self')


    #def __self__(self):
      #  return f'My name is {self.Name}. I am from {self.Address}. my phone number and email are {self.Phone} and {self.Email}. {self.describe}'
        





  
    
