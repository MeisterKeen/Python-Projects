from django.db import models
from django.db.models import Manager

# Create your models here.

TITLE_CHOICES = {
    ('Mr.', 'Mr.'),
    ('Ms.', 'Ms.'),
    ('Mrs.', 'Mrs.'),
    ('Dr.', 'Dr.'),
}


class Profile(models.Model):
    title = models.CharField(max_length=50, choices=TITLE_CHOICES)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    objects: Manager = models.Manager()

    def __str__(self):
        return self.firstname
