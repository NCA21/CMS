from django.db import models

class It(models.Model):
    ip_last = models.CharField(max_length=30)
    ip_first = models.CharField(max_length=30)
    ip_MRN = models.IntegerField()
    ip_cg = models.IntegerField()
    ip_tg = models.IntegerField()

class Nit(models.Model):
    p_last = models.CharField(max_length=30)
    p_first = models.CharField(max_length=30)
    p_MRN = models.IntegerField()
    p_cg = models.IntegerField()
    p_tg = models.IntegerField()

class Nurses(models.Model):
    n_last = models.CharField(max_length=30)
    n_first = models.CharField(max_length=30)
    n_UNIT = models.IntegerField()

