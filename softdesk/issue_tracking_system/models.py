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


#
# Initialization : Issue model
# 
class Issue(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name_plural = "Issues"

    def __str__(self):
        return self.title


#
# Initialization : Comment model
# 
class Comment(models.Model):
    description = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.description
