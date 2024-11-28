from django.db import models

class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.TextField(max_length=255)
