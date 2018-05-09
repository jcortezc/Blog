# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#   Modelo que hace referencia a los usuarios de django
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import *

# Clase PerfilUsuario


class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=300)
    usuario = models.OneToOneField(User)

    def __str__(self):
        return '%s' % self.nombre


class Post (models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    cuerpo = RichTextField();
    publicado = models.DateTimeField(auto_now_add=True)
    presentar = models.BooleanField(blank = True, null = False, default=True)
    autor = models.ForeignKey(PerfilUsuario)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

            super(Post, self).save(*args, **kwargs)