from django.db import models

# Create your models here.
class Empl(models.Model):
    eid=models.CharField(max_length=200)
    ename=models.CharField(max_length=200)
    epassword=models.IntegerField()
    esalary=models.IntegerField()
    eemail=models.EmailField(default="@gmail.com")
    econtact=models.CharField(max_length=30)
    def __str__(self):
        return self.ename