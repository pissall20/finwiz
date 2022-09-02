from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.email


class Service(models.Model):
    heading_text = models.CharField(max_length=200)
    description_text = models.TextField(max_length=2000)
    order = models.IntegerField(null=True)
    icon = models.CharField(max_length=30, default="bx bx-file")

    def __str__(self):
        return self.heading_text


class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="client_logos/", blank=True, null=True)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=2000)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.question


CLIENT_TYPE = (
    ("Corporate", "Corporate"),
    ("Retail", "Retail")
)


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="client_logos/", blank=True, null=True)
    video_link = models.CharField(max_length=200)
    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    short_desc = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="team_pictures/", null=True, blank=True)
    order = models.IntegerField(null=True)

    # social media
    twitter = models.CharField(max_length=200, default="#")
    facebook = models.CharField(max_length=200, default="#")
    instagram = models.CharField(max_length=200, default="#")
    linkedin = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.name
