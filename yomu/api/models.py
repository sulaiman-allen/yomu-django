from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)
    playlist = models.CharField(max_length=200)

    def __str__(self):
        return "{}: {}".format(self.id, self.title)

    def __unicode__(self):
        return "{}: {}".format(self.id, self.name)


