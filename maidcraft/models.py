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
    mobileNumber = models.PositiveBigIntegerField()
    adhaar = models.PositiveBigIntegerField()
    class Meta:
        abstract = True

class address(models.Model):
    doorNo = models.PositiveIntegerField()
    pinCode = models.PositiveBigIntegerField()
    area1 = models.CharField(max_length=255)
    area2 = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    class Meta:
        abstract = True

class bankDetails(models.Model):
    bankName = models.CharField(max_length=255)
    accountNumber = models.PositiveBigIntegerField()
    accountName = models.CharField(max_length=255)
    ifsc=models.CharField(max_length=15)
    upiId = models.CharField(max_length=255)
    class Meta:
        abstract = True


class maids(generalDetails):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name

class customer(generalDetails):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    apartmentName = models.CharField(max_length=255)
    towerNo = models.PositiveIntegerField()
    flatNumber = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class maidsAddress(address):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    maidsid = models.ForeignKey(maids,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class customerAddress(address):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    customerId = models.ForeignKey(customer,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class maidsBank(bankDetails):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    maidsid = models.ForeignKey(maids,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class customerBank(bankDetails):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    maidsid = models.ForeignKey(customer,on_delete=models.CASCADE)
    def __str__(self):
        return self.name