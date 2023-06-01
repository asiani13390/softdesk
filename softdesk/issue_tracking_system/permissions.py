from rest_framework.permissions import BasePermission
from .models import Project
from .models import Contributor



class AuthorAndContributorOnlyForProjects(BasePermission):


    def has_object_permission(self, request, view, obj):
        user = request.user
        
        project_id = view.kwargs.get('project_id')
        if (view.kwargs.get('pk') != None ):
            project_id = view.kwargs.get('pk')


        print("View action = ", view.action)
        print("User = ", user)
        print("Object author =", obj.author)


        if view.action == 'retrieve':
            print(">PERMISSION : AuthorAndContributorOnly_Retrieve() on project ", project_id)

            if (user == obj.author): 
                print("Author is authorized")
                return True
            
        if view.action == 'update':
            print(">PERMISSION : AuthorAndContributorOnly_Update() on project ", project_id)

            if (user == obj.author): 
                print("Author is authorized")
                return True

        if view.action == 'destroy':
            print(">PERMISSION : AuthorAndContributorOnly_Delete() on project ", project_id)

            if (user == obj.author): 
                print("Author is authorized")
                return True

        print("Not Author, Not Contributor")
        return False
