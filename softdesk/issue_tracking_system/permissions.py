from rest_framework.permissions import BasePermission
from .models import Project
from .models import Contributor
from django.shortcuts import get_object_or_404

# PERMISSION FOR ENDPOINT : Project
#
# Endpoint :
#           /projects/
#           /projects/{id}
#
# 3. GET - Retrieve the list of all the projects attached to the connected user (filtered by queryset)
# 4. POST - Create a project (All authenticated users)
# 5. GET - Retrieve project details from its id (Author or Contributor)
# 6. PUT - Update a project (Author only)
# 7. DELETE - Delete a project and its problems (Author only)
#
class PermissionProject(BasePermission):

    # RULES
    # A project is only accessible to its manager and contributors
    # Only an author can update and delete a project

    def has_permission(self, request, view):
        user = request.user

        print("> Permission_Project(has_permission) - Action : ", view.action, " User : ",user )

        # 3. GET - Retrieve the list of all the projects attached to the connected user
        if view.action == "list":
            print("Action : List")
            print("User is authenticated.")
            print("Return projects where user is contributor or author. It is filtered by queryset")
            print("Always authorized.")
            return True

        # 4. POST - Create a project
        if view.action == "create":
            print("Action : Create")
            print("User is authenticated.")
            print("Authenticated user can create a project.")
            return True

        # 5. GET - Retrieve project details from its id
        if view.action == "retrieve":
            print("Action : Retrieve")
            print("retrieve will be process in has_object_permission()")
            return True

        # 6. PUT - Update a project
        if view.action == "update":
            print("Action : Update")
            print("Update will be process in has_object_permission()")
            return True

        # 7. DELETE - Delete a project and its problems
        if view.action == "destroy":
            print("Action : Destroy")
            print("destroy will be process in has_object_permission()")
            return True
        
        # End of this permission class 
        print("> Permission_Project(has_permission) is finished.")
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        print("> Permission_Project(has_object_permission) : View action = ", view.action, "User = ", user, "Object author =", obj.author)
        

        if view.action == "list":
            print("Action : List")
            return True

        if view.action == "create":
            print("Action : Create")
            return True

        if view.action == "update":
            print("Action : Update")
            print("Only project author is able to update a project.")

            if (user == obj.author): 
                print("User is the author. Author is authorized.")
                return True
            else:
                print("User is not the project author : Not autorized")
                return False

        if view.action == "destroy":
            print("Action : Destroy")
            print("Only project author is able to delete a project.")

            if (user == obj.author): 
                print("User is the author. Author is authorized.")
                return True
            else:
                print("User is not the project author : Not autorized")
                return False

        if view.action == "retrieve":
            print("Action : Retrieve")
            print("Author and Contributor are able to retrieve a project.")

            if (user == obj.author): 
                print("User is author. Author is authorized.")
                return True

            if (user in obj.contributors.all()):
                print("User is a contributor. Contributor is authorized.")
                return True
            
            # Permission denied
            print("Not Author, Not Contributor : Permission denied.")
            return False


        print("> Permission_Project(has_object_permission) is finished. True is returned because need to check others permissions.")
        return True


# PERMISSION FOR ENDPOINT
#
# Endpoint :
#           /projects/{id}/users/
#           /projects/{id}/users/{id}
#
# 8.  POST - Add a collaborator to a project (Author only)
# 9.  GET - Retrieve the list of all users attached to a project (Author or Contributor)
# 10. DELETE - Remove a user from a project (Author only)
#
class PermissionProjectsUsers(BasePermission):

    # RULES
    # 
    # 

    def has_permission(self, request, view):
        user = request.user

        print("> Permission_xxx(has_permission) - Action : ", view.action, " User : ", user )

        if view.action == "list":
            print("Action : List")
            print("Only project author or contributor are able to list users attached to a project.")
            
            project_id = view.kwargs.get('project_id')
            project = Project.objects.get(id=project_id)

            if user == project.author:
                print("User is the project author : Author is authorized (Project_id : ", project_id,")")
                "Project_id : ", project_id
                return True

            if Contributor.objects.filter(user=user, project=project).exists():
                print("User is a project contributor : Contributor is authorized to list. (Project_id : ", project_id,")")
                return True

            print("User is not the author and not a contributor, user is not authorized.")
            return False


        if view.action == "create":
            print("Action : Create")
            print("Only project author is able to add contributor.")
            
            project_id = view.kwargs.get('project_id')
            project = Project.objects.get(id=project_id)

            if user == project.author:
                print("User is the project author : Author is authorized (Project_id : ", project_id,")")
                "Project_id : ", project_id
                return True
            
            print("User is not the project author : User is not authorized (Project_id : ", project_id,")")
            return False


        if view.action == "update":
            print("Action : Update")
            print("No update function available.")
            return False
            
        if view.action == "destroy":
            print("Action : Destroy")
            print("Only project author is able to delete a contributor.")

            project_id = view.kwargs.get('project_id')
            project = Project.objects.get(id=project_id)

            if user == project.author:
                print("User is the project author : Author is authorized (Project_id : ", project_id,")")
                "Project_id : ", project_id
                return True
            
            print("User is not the project author : User is not authorized (Project_id : ", project_id,")")
            return False


        if view.action == "retrieve":
            print("Action : Retrieve")
            print("No retrieve function is available.")
            return False

        print("> Permission_xxx(has_permission) is finished. True is returned because need to check others permissions.")
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        print("> Permission_xxx(has_object_permission) : View action = ", view.action, "User = ", user, "Object author =", obj.author)
        

        if view.action == "list":
            print("Action : List")
           
        if view.action == "create":
            print("Action : Create")
           
        if view.action == "update":
            print("Action : Update")
           
        if view.action == "destroy":
            print("Action : Destroy")
           
        if view.action == "retrieve":
            print("Action : Retrieve")                       


        print("> Permission_xxx(has_object_permission) is finished. True is returned because need to check others permissions.")
        return True


# PERMISSION FOR ENDPOINT
#
# Endpoint :
#           /projects/{id}/issues/
#           /projects/{id}/issues/{id}
#
# 11. GET - Retrieve the list of problems related to a project (Contributor only)
# 12. POST - Creating a problem in a project (Contributor)
# 13. PUT - Update a problem in a project (Author only)
# 14. DELETE - Delete a problem from a project (Author only)
#
class PermissionIssue(BasePermission):

    # RULES
    # 
    # 

    def has_permission(self, request, view):
        user = request.user

        print("> Permission_Issue(has_permission) - Action : ", view.action, " User : ", user )

        if view.action == "list":
            print("Action : List")
            print("Contributor only is able to display the issue.")

            project_id = view.kwargs.get('project_id')

            print("Project_id :", project_id)

            project = get_object_or_404(Project, id=project_id)

            if Contributor.objects.filter(user=user, project=project).exists():
                print("User is a project contributor : Contributor is authorized to list. (Project_id : ", project_id,")")
                return True
            
            print("User is a not a project contributor : User is not authorized to list. (Project_id : ", project_id,")")
            return False


        if view.action == "create":
            print("Action : Create")
            print("Project contributor only can create Issue")

            project_id = view.kwargs.get('project_id')

            print("Project_id :", project_id)

            project = get_object_or_404(Project, id=project_id)

            if Contributor.objects.filter(user=user, project=project).exists():
                print("User is a project contributor : Contributor is authorized to create. (Project_id : ", project_id,")")
                return True
            
            print("User is a not a project contributor : User is not authorized to create. (Project_id : ", project_id,")")
            return False


        if view.action == "update":
            print("Action : Update")
            
        if view.action == "destroy":
            print("Action : Destroy")

        if view.action == "retrieve":
            print("Action : Retrieve")

        print("> Permission_Issue(has_permission) is finished. True is returned because need to check others permissions.")
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        print("> Permission_Issue(has_object_permission) : View action = ", view.action, "User = ", user, "Object author =", obj.author)
        

        if view.action == "list":
            print("Action : List")
           
        if view.action == "create":
            print("Action : Create")
           
        if view.action == "update":
            print("Action : Update")
            print("User must be a project contributor.")
            print("Only issue author can update the issue.")

            project_id = view.kwargs.get('project_id')
            project = get_object_or_404(Project, id=project_id)

            if Contributor.objects.filter(user=user, project=project).exists():
                print("User is a project contributor. (Project_id : ", project_id,")")

                if user == obj.author:
                    print("User is the issue author. User is authorized.")
                    return True
                else:
                    print("User is not the issue author. User is unauthorized.")
                    return False

            else:
                print("User is a not a project contributor. (Project_id : ", project_id,")")
                print("User is not authorized.")
                return False

           
        if view.action == "destroy":
            print("Action : Destroy")
            print("User must be a project contributor.")
            print("Only issue author can delete the issue.")

            project_id = view.kwargs.get('project_id')
            project = get_object_or_404(Project, id=project_id)

            if Contributor.objects.filter(user=user, project=project).exists():
                print("User is a project contributor. (Project_id : ", project_id,")")

                if user == obj.author:
                    print("User is the issue author. User is authorized.")
                    return True
                else:
                    print("User is not the issue author. User is unauthorized.")
                    return False

            else:
                print("User is a not a project contributor. (Project_id : ", project_id,")")
                print("User is not authorized.")
                return False


        if view.action == "retrieve":
            print("Action : Retrieve")                       


        print("> Permission_Issue(has_object_permission) is finished. True is returned because need to check others permissions.")
        return True


# PERMISSION FOR ENDPOINT
#
# Endpoint :
#           /projects/{id}/issues/{id}/comments/
#           /projects/{id}/issues/{id}/comments/{id}
#
# 15. POST - Create comments on a problem (Author or Contributor)
# 16. GET - Retrieve the list of all comments related to a problem (Author or Contributor)
# 17. PUT -  Edit a comment (Author only)
# 18. DELETE - Delete a comment (Author only)
# 19. GET - Get a comment via its id (Author or Contributor)

class PermissionComment(BasePermission):

    # RULES
    # 
    # 

    def has_permission(self, request, view):
        user = request.user

        print("> Permission_Comment(has_permission) - Action : ", view.action, " User : ", user )

        if view.action == "list":
            print("Action : List")
            print("Only project contributors or the project's author can list comments")

            project_id = view.kwargs.get('project_id')
            project = get_object_or_404(Project, id=project_id)

            if user == project.author:
                return True

            if Contributor.objects.filter(user=user, project=project).exists():
                print("User is a project contributor. (Project_id : ", project_id,")")
                return True
            else:
                print("User is a not a project contributor. (Project_id : ", project_id,")")
                print("User is not authorized.")
                return False

        if view.action == "create":
            print("Action : Create")
            print("Only project contributors can create comments")

            project_id = view.kwargs.get('project_id')
            project = get_object_or_404(Project, id=project_id)

            if Contributor.objects.filter(user=user, project=project).exists():
                print("User is a project contributor. (Project_id : ", project_id,")")
                return True
            else:
                print("User is a not a project contributor. (Project_id : ", project_id,")")
                print("User is not authorized.")
                return False

        if view.action == "update":
            print("Action : Update")
            
        if view.action == "destroy":
            print("Action : Destroy")

        if view.action == "retrieve":
            print("Action : Retrieve")

        print("> Permission_Comment(has_permission) is finished.")
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        print("> Permission_Comment(has_object_permission) : View action = ", view.action, "User = ", user, "Object author =", obj.author)
        

        if view.action == "list":
            print("Action : List")
           
        if view.action == "create":
            print("Action : Create")
           
        if view.action == "update":
            print("Action : Update")
            print("Only comment's author can update comment")

            if user == obj.author:
                print("User is the comment's author. User is authorized.")
                return True
            else:
                print("User is not the comment's author. User is not authorized.")
                return False
           
        if view.action == "destroy":
            print("Action : Destroy")
            print("Only comment's author can delete comment")

            if user == obj.author:
                print("User is the comment's author. User is authorized.")
                return True
            else:
                print("User is not the comment's author. User is not authorized.")
                return False


        if view.action == "retrieve":
            print("Action : Retrieve")
            print("Only project contributors or the project's author can read comments")

            project_id = view.kwargs.get('project_id')
            project = get_object_or_404(Project, id=project_id)

            if user == project.author:
                print("User is the project's author. User is authorized.")
                return True
            else:
                print("User is not the project's author.")

            if Contributor.objects.filter(user=user, project=project).exists():
                print("User is a project contributor. (Project_id : ", project_id,")")
                return True
            else:
                print("User is a not a project contributor. (Project_id : ", project_id,")")
                print("User is not authorized.")
                return False



        print("> Permission_Comment(has_object_permission) is finished. True is returned because need to check others permissions.")
        return True

