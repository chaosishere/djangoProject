from django.db import models

# Create your models here.
# just cahnging authors check
class Room(models.Model):
    #host =
    #topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participations
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
