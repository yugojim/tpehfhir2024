# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:33:36 2022

@author: yugojim
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Permission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 20)
    patient=models.BooleanField()
    emergency=models.BooleanField()
    outpatient=models.BooleanField()
    inpatient=models.BooleanField()
    medication=models.BooleanField()
    report=models.BooleanField()
    administrative=models.BooleanField()
    up=models.BooleanField()
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    def __str__(self):
        #return self.user 
        return f'{self.id} {self.user} {self.title}\
            病人資料 {self.patient} 急診 {self.emergency} 門診 {self.outpatient} 住診 {self.inpatient}\
                用藥 {self.medication} 報告 {self.report} 行政 {self.administrative} 上傳{self.up}\
                    修改時間{self.dateTimeOfUpload}'

class fhirip(models.Model):
    location = models.CharField(max_length = 50)
    ip = models.CharField(max_length = 50)
    token = models.CharField(max_length = 200)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    def __str__(self):
        #return self.user 
        return f'{self.id} {self.location} {self.ip} \
             {self.token} 修改時間{self.dateTimeOfUpload}'
             
class UserLoginRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_records')
    login_time = models.DateTimeField(default=now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} logged in at {self.login_time}"