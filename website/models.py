from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.email


class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="client_logos/", blank=True, null=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=2000)

    def __str__(self):
        return self.question


CLIENT_TYPE = (
    ("Corporate", "Corporate"),
    ("Retail", "Retail")
)


class PortFolio(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="client_logos/", blank=True, null=True)
    video_link = models.CharField(max_length=200)
    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE)

    def __str__(self):
        return self.name

