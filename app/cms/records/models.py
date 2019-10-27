from django.db import models

class It(models.Model):
    ip_last = models.CharField(max_length=30, blank=True, default='')
    ip_first = models.CharField(max_length=30, blank=True,  default='')
    ip_MRN = models.IntegerField(blank=True,  default=0)
    ip_cg = models.IntegerField(blank=True,  default=100)
    ip_tg = models.IntegerField(blank=True,  default=180)
    def intro(self):
        return "Patient {} {}".format(self.ip_first, self.ip_last)

class Nit(models.Model):
    p_last = models.CharField(max_length=30, blank=True,  default='')
    p_first = models.CharField(max_length=30, blank=True,  default='')
    p_MRN = models.IntegerField(blank=True, default=0)
    p_cg = models.IntegerField(blank=True, default=100)
    p_tg = models.IntegerField(blank=True, default=180)
    def stat(self):
        return "Patient {} has stable BG of {}".format(self.p_MRN, self.p_cg)

class Nurses(models.Model):
    n_last = models.CharField(max_length=30, blank=True,  default='')
    n_first = models.CharField(max_length=30, blank=True,  default='')
    n_UNIT = models.IntegerField(blank=True, default=1)
    def assign(self):
        return "Nurse {} is staffing Unit {}".format(self.n_last, self.n_UNIT)
