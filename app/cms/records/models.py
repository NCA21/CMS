from django.db import models

class Doctor(models.Model):
    doc_first = models.CharField(max_length=30)
    doc_last  = models.CharField(max_length=30)
    ID = models.IntegerField()

class Patient(models.Model):
    patient_first = models.CharField(max_length=30)
    patient_last = models.CharField(max_length=30)
    ethnicity = models.CharField(max_length=30)
    AGE = models.IntegerField()
    MEID = models.IntegerField()

class Contact(models.Model):
    contact_first = models.CharField(max_length=30)
    contact_last = models.CharField(max_length=30)
    contact_PHONE = models.IntegerField()
