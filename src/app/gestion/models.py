# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Service(models.Model):
    type=models.TextField(max_length=50)




class TypePetition(models.Model):
    name=models.TextField(max_length=100)


class Petition(models.Model):
    date=models.DateField()
    message=models.TextField(max_length=200)
    service_id=models.ForeignKey(Service, on_delete=models.CASCADE)
    type_petition_id=models.ForeignKey(TypePetition, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)

class Gallery(models.Model):
    image=models.FileField()
    service_id=models.ForeignKey(Service,on_delete=models.CASCADE)

