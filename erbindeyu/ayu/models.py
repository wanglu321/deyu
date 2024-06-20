from django.db import models

# Create your models here.
class Message(models.Model):
   名字 = models.CharField(max_length=200) 
   留言 = models.CharField(max_length=1000)
   
   def __str__(self):
      return self.名字 + ' ' + self.留言