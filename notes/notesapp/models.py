import re
from django.db import models
from django.contrib.auth.models import User


class Home_notes(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.title


class Subjectby_notes(models.Model):
    home_notes = models.ForeignKey(Home_notes, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    actual_price = models.IntegerField()
    discounted_price = models.IntegerField()

    def __str__(self):
        return self.title


class Payments_details(models.Model):
    pay_amount = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Download_pdf(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    subjectby_notes = models.ForeignKey(
        Subjectby_notes, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='media')
    is_approved = models.BooleanField(default=False)
    verbose_name = "upload_notes"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "upload_notes"


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=500, blank=True, null=True)
    message = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
