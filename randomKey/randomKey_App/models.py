from django.db import models

class Keyrecord(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=15)
    
