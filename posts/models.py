from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
# Relational database -> Tables
class Post(models.Model):
    title = models.CharField(max_length=128) # String
    subtitle = models.CharField(max_length=128) # String
    body = models.TextField() # String
    created_on = models.DateTimeField(auto_now_add=True) # DateTime
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self): # to String method
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        # Automatically redirect the user to a specific endpoint after a POST request is made   
        return reverse('post_detail', args=[str(self.id)])
    status = models.ForeignKey(
        "Status",
        on_delete=models.CASCADE,
    )

class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"    

    name = models.CharField(max_length=128, unique=True) 
    description = models.CharField(max_length=256, help_text="Write a description about the status")

    def __str__(self): 
        return f"Status (ID= {self.id} - Name= {self.name} - Description= {self.description[:25]}...)"