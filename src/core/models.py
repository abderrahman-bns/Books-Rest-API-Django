from django.db import models

class Books(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=150,) 
    subtitle = models.CharField(max_length=150,)   
    author = models.CharField(max_length=100,)               
    published = models.DateTimeField()
    publisher = models.CharField(max_length=100,)      
    pages = models.IntegerField()
    description = models.TextField()
    website = models.CharField(max_length=150,)  
    
    def __str__(self):
        return self.title
    