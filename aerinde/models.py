from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class List(models.Model):
    name = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, related_name='lists', null=True)

    def __unicode__(self):
        return unicode(self.name)


class Task(models.Model):
    task = models.CharField(max_length=100, null=True)
    deadline = models.CharField(max_length=100, null=True)
    list = models.ManyToManyField(List, related_name="tasks")
    user = models.ForeignKey(User, related_name='jobs', null=True)

    def __unicode__(self):
        return unicode(self.job)

#class Location(models.Model):
 #   destination = models.OneToOneField(Destination, related_name="locations")

  #  def __unicode__(self):
#        return unicode(self.destination)