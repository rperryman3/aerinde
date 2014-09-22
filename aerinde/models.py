from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    username = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100, null=True)
    def __unicode__(self):
        return unicode(self.username)

