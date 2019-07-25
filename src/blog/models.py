from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=255)
    rec_time = models.DateTimeField()
    content = models.TextField()
    def __str__(self):
        return self.title
