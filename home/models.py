from django.db import models
from django.utils import timezone

# Create your models here.

class user(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.TextField()
    email=models.EmailField()
    address=models.TextField(default='')
    timestamp=models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.username