from django.db import models

# Create your models here.
class Base_contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    content = models.TextField()  # Ensure this field is defined


    def __str__(self):
        return self.name
    