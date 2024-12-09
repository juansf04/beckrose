# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Plantas(models.Model):
    id_planta = models.IntegerField(primary_key=True)
    nome_planta = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'plantas'


class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'


class UserPlantas(models.Model):
    id_user = models.OneToOneField(User, models.DO_NOTHING, db_column='id_user', primary_key=True)  # The composite primary key (id_user, id_planta) found, that is not supported. The first column is selected.
    id_planta = models.ForeignKey(Plantas, models.DO_NOTHING, db_column='id_planta')

    class Meta:
        managed = False
        db_table = 'user_plantas'
        unique_together = (('id_user', 'id_planta'),)
