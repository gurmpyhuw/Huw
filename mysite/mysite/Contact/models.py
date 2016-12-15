from django.db import models
import datetime

# Create your models here.
#class Publisher(models.Model):
#    name = models.CharField(max_length=30)
#    address = models.CharField(max_length=50)
#    city = models.CharField(max_length = 60)
#    state_province = models.CharField(max_length = 30)
#    country = models.CharField(max_length = 50)
#    website = models.URLField()
#    def __str__(self):
#        return self.name

#class Meta:
#    ordering = ['name']

#class Author(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=40)
#    email = models.EmailField(blank=True, verbose_name='e-mail')
#    def __str__(self):
#        return u'%s %s' % (self.first_name, self.last_name)

#class Book(models.Model):
#    title = models.CharField(max_length=100)
#    authors = models.ManyToManyField(Author)
#    publisher = models.ForeignKey(Publisher)
#    publication_date = models.DateField(blank=True, null=True)
#    def __str__(self):
#        return self.title

class Title(models.Model):
    Name = models.CharField(max_length = 10)

class Region(models.Model):
    Name = models.CharField(max_length = 4)
    Description = models.CharField(max_length = 25)

class Relationship(models.Model):
    Name = models.CharField(max_length = 25)

class JobTitle(models.Model):
    JobName = models.CharField(max_length = 25)

class Type(models.Model):
    TypeName = models.CharField(max_length=25)

class Interest(models.Model):
    ShortName = models.CharField(max_length = 3)
    FullName = models.CharField(max_length = 25)

class Source(models.Model):
    Type = models.ForeignKey(Type)
    Source = models.CharField(max_length = 50)
    SourceInfo = models.CharField(max_length = 100)
    Interest = models.ForeignKey(Interest)

class Contact(models.Model):
    DtAdded = models.DateField()
    Title = models.ForeignKey(Title)
    FirstName = models.CharField(max_length = 25)
    LastName = models.CharField(max_length = 50)
    Email = models.EmailField()
    Region = models.ForeignKey(Region)
    Interests = models.ManyToManyField(Interest)
    Relationship = models.ForeignKey(Relationship)
    JobTitle = models.ForeignKey(JobTitle)