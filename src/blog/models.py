from django.db import models
from UserProfile.models import UserProfile

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=255)
    rec_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    poster = models.ForeignKey(UserProfile, related_name='posts', on_delete = models.CASCADE)
    def __str__(self):
        return self.title
