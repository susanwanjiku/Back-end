from django.db import models

# Create your models here.
class Course(models.Model):
    names = models.CharField(max_length = 30)
    Course = models.CharField(max_length = 30)
    description = models.CharField(max_length = 30)
    def __str__ (self):
        return self.names
    