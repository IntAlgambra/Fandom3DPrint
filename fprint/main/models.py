from django.db import models
from django.utils import timezone
from datetime import datetime

class Question(models.Model):
    sender_name = models.CharField(max_length=200)
    sender_email = models.EmailField()
    question_text = models.TextField()
    question_file = models.FileField(upload_to='clients_files/', blank=True)
    question_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        question_info = 'sender: {0}, date: {1}'.format(self.sender_name, self.question_time)
        return question_info

class PrintingOrder(models.Model):

    MATERIALS = [
        ('PLA', 'PLA'),
        ('ABS', 'ABS'),
        ('PETG', 'PETG'),
        ('NEYLON', 'NEYLON'),
        ('FLEX', 'FLEX'),
    ]

    QUALITY = [
        ('HIGH', 'High, 0.1mm layer height'),
        ('MEDIUM', 'Medium, 0.2mm layer height'),
        ('LOW', 'Low, 0.3mm layer height')
    ]
    
    sender_name = models.CharField(max_length=200)
    sender_email = models.EmailField()
    material = models.CharField(max_length = 10, choices = MATERIALS)
    quality = models.CharField(max_length = 6, choices = QUALITY)
    color = models.CharField(max_length=100, blank=True)
    order_file = models.FileField(upload_to='printing_orders_files')
    order_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        order_info = 'sender: {0}, date: {1}'.format(self.sender_name, self.sender_email)
        return order_info

class ModelingOrder(models.Model):

    sender_name = models.CharField(max_length=200)
    sender_email = models.EmailField()
    order_description = models.TextField(blank=True)
    order_file = models.FileField(upload_to='modeling_orders_files')
    order_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        order_info = 'sender: {0}, date: {1}'.format(self.sender_name, self.sender_email)
        return order_info
