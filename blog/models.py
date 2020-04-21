from django.db import models

class Blog(models.Model):
    title = models.TextField(max_length=250)
    date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return self.title
