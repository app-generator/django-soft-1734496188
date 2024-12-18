# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    funcion = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Operador(models.Model):

    #__Operador_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Operador_FIELDS__END

    class Meta:
        verbose_name        = _("Operador")
        verbose_name_plural = _("Operador")


class Areas(models.Model):

    #__Areas_FIELDS__
    idoperador = models.ForeignKey(operador, on_delete=models.CASCADE)

    #__Areas_FIELDS__END

    class Meta:
        verbose_name        = _("Areas")
        verbose_name_plural = _("Areas")


class Parcela(models.Model):

    #__Parcela_FIELDS__
    estado = models.CharField(max_length=255, null=True, blank=True)
    nc = models.CharField(max_length=255, null=True, blank=True)

    #__Parcela_FIELDS__END

    class Meta:
        verbose_name        = _("Parcela")
        verbose_name_plural = _("Parcela")


class Conceptos(models.Model):

    #__Conceptos_FIELDS__
    idarea = models.ForeignKey(areas, on_delete=models.CASCADE)

    #__Conceptos_FIELDS__END

    class Meta:
        verbose_name        = _("Conceptos")
        verbose_name_plural = _("Conceptos")



#__MODELS__END
