from django.db import models

# Create your models here.

# 
# Initialization : Project model
#
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

