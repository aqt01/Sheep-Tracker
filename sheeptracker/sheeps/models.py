from django.db import models


ROLES= (
('1','Invitado'),
('2', 'Miembro'),
('3', 'Lider'),
('4','Pastor/a'),
('5','Pastor/a general'),)




# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    e_mail=models.EmailField()
    cellphone=models.CharField(max_length=15)
    tellphonne=models.CharField(max_length=15)

    class meta:
        abstract= True

class Address(models.Model):
    country=models.CharField("Pais",max_length=60) # This can be changed to an external field?
    state=models.CharField("Estado/Pronvicia",max_length=60)
    area=models.CharField("Area",max_length=60)
    street=models.CharField("Calle",max_length=60)
    home=models.CharField("# Casa", max_length=60)
    perimeter=models.IntegerField('Perimetro')
    # geolocation=

    class meta:
        abstract = True

class Person(Contact , Address):
    cell = models.ForeignKey()
    organization = models.ForeignKey('Iglesia u organizacion', max_length=80)
    role= models.CharField('Rol',choices=ROLES,max_length=80)
    pic = models.FileField()


    def __unicode__(self):
        return '%s %s' % (self.name)

