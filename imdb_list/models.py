from django.db import models

# Create your models here.
class WatchList(models.Model):
    name = models.CharField(max_length=100)
    storyline = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name