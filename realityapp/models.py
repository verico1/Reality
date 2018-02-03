# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class call_us(models.Model):
    name = models.CharField("first name and last name", max_length=60)
    email = models.CharField("email who that sent message", max_length=60)
    phonenumber = models.CharField("phone number who that sent message", max_length=12)
    content = models.TextField("Sender's message")
