from django.db import models

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date_posted = models.DateTimeField()
    content = models.TextField

    def __str__(self):
        return self.title
