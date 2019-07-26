from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=40)
    img = models.ImageField(upload_to="profile", null=True, blank=True)
    def __str__(self):
        return self.name
