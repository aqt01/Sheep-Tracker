from django.db import models

from django.contrib.auth.models import User

ROLES= (
(1,'Guest'),
(2,'Member'),
(3,'Leader'),
(4,'Pastor'),
(5,'Minister'),
(6,'Elder'),
(7,'Titular pastor'),
)



# we must connect this with geomap
class Address(models.Model):
    country=models.CharField("Country",max_length=60) # This can be changed to an external field?
    state=models.CharField("State/Province",max_length=60)
    area=models.CharField("Area",max_length=60)
    street=models.CharField("Street",max_length=60)
    home=models.CharField("# ", max_length=60)
    perimeter=models.IntegerField('Perimeter',null=True) # must hide this is not for this release
    # geolocation=

    class meta:
        abstract = True

class Contact(Address):
    first_name = models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    e_mail=models.EmailField()
    cellphone=models.CharField(max_length=15)
    tellphone=models.CharField(max_length=15)
    birthdate=models.DateField('Birthdate')

    class meta:
        abstract= True


class Organization(models.Model):
    name =  models.CharField('Name',max_length=120)
    e_mail = models.CharField('E-mail',max_length=120)

    country=models.CharField("Country",max_length=60) # This can be changed to an external field?
    state=models.CharField("State/Province",max_length=60)
    area=models.CharField("Area",max_length=60)
    street=models.CharField("Street",max_length=60)
    home=models.CharField("# ", max_length=60)
    perimeter=models.IntegerField('Perimeter',null=True) # must hide this is not for this release
    # geolocation=
    #staff= models.ManyToManyField(Person) # Church staff ?
    # need social media connections


class Person(Contact):
    user = models.OneToOneField(User)
    role= models.CharField('Role',choices=ROLES,max_length=80)
    pic = models.FileField()
    organization_visit = models.ForeignKey(Organization,related_name='organization_person')
    timestamp=models.DateField(auto_now=True) 

    def __unicode__(self):
        return '%s %s' % (self.name)




# CELL
PLACES= (
(1,'Iglesia principal'),
(2,'Iglesia'),
(3,'Celula'),
)

class Location(Address):
    name =  models.CharField('Name',max_length=120)
    guests = models.ManyToManyField(Person,max_length=120,related_name='guests') #this are members if cell is chosen as church
    consolidators= models.ManyToManyField(Person,related_name='consolidators') # Church staff ?
    supervisor = models.ManyToManyField(Person,related_name='supervisors') # Person in charge
    place= models.CharField('Place',choices=PLACES,max_length=80)
    organization = models.ForeignKey(Organization,related_name='organization_cell')
    # we need a schedule for the cell


# must heredate from userprofile
class AssistanceAvg(models.Model):
    attendance_avg=models.FloatField('avrg of attendance') #Assist avrg of a particular cell
    start_date=models.DateField('From') # the created date of the cell
    end_date=models.DateField('To') # the last checked attendance
         
# every saved instance
class Assistance(models.Model):
    location=models.ForeignKey(Location)
    attendance_avg=models.FloatField('promedio de asistencia') #Assis average
    timestamp=models.DateField(auto_now=True) 
    guests=models.ManyToManyField(Person)

# every saved instance on attendance will recalculate the attendance avg for their cell
