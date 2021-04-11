from django.db import models
from django.db.models import Manager

# Create your models here.


class DjangoClasses(models.Model):
    title = models.CharField(max_length=100)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=100)
    Duration = models.FloatField()

    objects: Manager = models.Manager()

    def __str__(self):
        return self.title # Name of object will display as course title


# I created three objects using the admin interface. Can I instantiate objects right here?
a = DjangoClasses(title="Hacky Tacky Solutions", courseNumber="88", instructorName="Goofus Doofus", Duration="6.66")
a.save()

# HAHAHA, it spawned SIX of this object.
# So now, every time Django routinely checks models.py, it makes a new "Hacky Tacky Solutions" object
# This is so funny I'm leaving it in
# HACKY TACKY SOLUTIONS TO THE MOON, BOYS
