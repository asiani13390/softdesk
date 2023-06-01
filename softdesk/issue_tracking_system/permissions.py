from rest_framework.permissions import BasePermission
from .models import Project
from .models import Contributor



class AuthorAndContributorOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        project_id = view.kwargs.get('project_id')

        print("View action = ", view.action)
        print("User = ", user)
        print("Object author =", obj.author)

        if view.action == 'retrieve':
            print("> PERMISSION (AuthorAndContributorOnly",str(project_id),")")
            if (request.user == obj.author): 
                print("Author is authorized")
                return True
            

        print("Not Author, Not Contributor")
        return False
