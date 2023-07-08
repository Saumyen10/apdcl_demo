from django.db import models

# Create your models here.
class connect (models.Model):
    name = models.CharField(max_length=30)
    pincode = models.IntegerField()
  
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    issue = models.TextField()

    def __str__(self):
        return self.name
   