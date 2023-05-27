from django.db import models
from django.contrib.auth.models import User 


# 
# Initialization : Project model
#
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_author")
    contributors = models.ManyToManyField(User, through="Contributor")

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title




#
# Initialization : Contributor model
# 
class Contributor(models.Model):

    PERMISSIONS = (
        ('admin', 'Administrator'),
        ('member', 'Member'),
        ('guest', 'Guest'),
    )

    permissions = models.CharField(max_length=255, choices=PERMISSIONS)
    role = models.CharField(max_length=255, null=True, blank=True, default='')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Contributors"
 
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
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
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
