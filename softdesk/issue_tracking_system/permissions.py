from rest_framework.permissions import BasePermission
from .models import Project
from .models import Contributor



class PermissionProject(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user

        print("> Permission_Project() : View action = ", view.action, "User = ", user, "Object author =", obj.author)
        
        # A project is only accessible to its author and contributors
        if view.action == 'retrieve':
            print(">PERMISSION : PermissionProject_Retrieve()")

            if (user == obj.author): 
                print("Author is authorized.")
                return True

            if (user in obj.contributors.all()): 
                print("Contributor is authorized.")
                return True


        if view.action == 'update':
            print(">PERMISSION : PermissionProject_Update()")

            if (user == obj.author): 
                print("Author is authorized")
                return True
 

        if view.action == 'destroy':
            print(">PERMISSION : PermissionProject_Destroy()")

            if (user == obj.author): 
                print("Author is authorized")
                return True


        print("Not Author, Not Contributor")
        return False
