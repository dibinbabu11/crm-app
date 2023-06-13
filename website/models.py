from django.db import models

# Create your models here.

class Record(models.Model):
    created_at=models.DateField(auto_now_add=True)
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    def __str__(self):
        return self.first_name
    

