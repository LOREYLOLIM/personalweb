from django.db import models

# Create your models here.


class Home(models.Model):
    Title = models.CharField(max_length = 100)
    Content = models.TextField()

def __str__(self):
    return self.Title

class About(models.Model):
    Title = models.CharField(max_length = 50)
    Message = models.TextField()
    Time = models.DateTimeField()

def __str__(self):
    return self.Title

class Contact(models.Model):

    Phone = models.IntegerField()
    Email = models.EmailField()
    Location = models.CharField(max_length = 50)

def __str__(self):
    return self.Email

class Service(models.Model):
    Title = models.CharField(max_length = 50)
    Message = models.TextField()
    Time = models.DateTimeField()

def __str__(self):
    return self.Title


class Testimonial(models.Model):
    Name = models.CharField(max_length = 50)
    Testimonial = models.TextField()

def __str__(self):
    return self.Name

class Update(models.Model):
    Title = models.CharField(max_length = 50)
    Message = models.TextField()
    Time = models.DateTimeField()

def __str__(self):
    return self.Title