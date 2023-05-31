from rest_framework.permissions import BasePermission
from .models import Project
from .models import Contributor

class CanEditOrDestroyProject(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        user = request.user

        if view.action == 'destroy':
            if (user == obj.author): 
                return True
            else:
                return False

        if view.action == 'update':
            if (user == obj.author): 
                return True
            else:
                return False


        return True


class CanAddContributorInProject(BasePermission):
    
    def has_permission(self, request, view):
        user = request.user

        if view.action == 'create':
            project_id = view.kwargs.get('project_id')
            project = Project.objects.get(id=project_id)

            if user == project.author:
                return True
            else:
                return False

        return True

      
class CanListContributorOfProject(BasePermission):
    
    def has_permission(self, request, view):
        user = request.user

        project_id = view.kwargs.get('project_id')
        project = Project.objects.get(id=project_id)

        
        if view.action == 'list':
            if Contributor.objects.filter(project_id=project_id, user=user).exists():
                return True
            
            if user == project.author:
                return True

        return True

class CanDestroyContributorOfProject(BasePermission):
    
    def has_permission(self, request, view):
            return True
    

# ISSUES 11.12.13.14
class IssueViewsetPermission(BasePermission):

    # 
    def has_permission(self, request, view):
        return True