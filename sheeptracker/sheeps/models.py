from django.db import models

# Create your models here.

class Cell(models.Model):
    organization = ForeignKey(Organization)
    address = OneToOneField(Address)

class SocialMedia(models.Model):
    name = models.CharField()
    contact = ForeignKey(Contact)
    
class Address(models.Model):
    

# this is meta
class Contact(models.Model):
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    # Should be replaced with number fields
    cellphone = models.CharField(max_length=10)
    telephone = models.CharField(max_length=10)
    pic = models.FileField()


class Member(Contact):
    organization = ForeignKey(Organization)
    
    
