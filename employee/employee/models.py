from django.db import models

class Employee(models.Model):
    # def nameFile(instance, filename):
    #     return '/'.join(['images', str(instance.name), filename])
    emp_id=models.AutoField(primary_key=True)
    emp_name=models.CharField(max_length=50)
    phone_no= models.IntegerField(default = 0)
    comp_name= models.CharField(max_length=300, default="")
    designation=models.CharField(max_length = 300,default="")
    location=models.CharField(max_length=300)
    image= models.ImageField(upload_to="media1/images",blank = True)


def __str__(self):
    return self.emp_name