from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    #make url accessible
    url = models.URLField(blank=False)


    def __str__(self):
        return self.title
