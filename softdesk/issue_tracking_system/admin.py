from django.contrib import admin

from .models import Project
from .models import Contributor
from .models import Issue
from .models import Comment

# Register your models here.

admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)

