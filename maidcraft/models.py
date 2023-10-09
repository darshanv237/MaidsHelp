from django.db import models
import uuid

# Create your models here.
# New concept learnt
# if we want to resuse the model we can create a abstract model 
# https://g.co/bard/share/65153fbf52d6

class generalDetails(models.Model):
    name  = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    mobileNumber = models.PositiveBigIntegerField(max_length=10)
    adhaar = models.PositiveBigIntegerField(max_length=12)
    class Meta:
        abstract = True

class Maids(generalDetails):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class customer(generalDetails):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    apartmentName = models.CharField(max_length=255)
    towerNo = models.PositiveIntegerField()
    flatNumber = models.PositiveIntegerField()

