from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.shortcuts import get_object_or_404

from .models import Project
from .models import Contributor
from .models import Issue


from .serializers import SignupSerializer
from .serializers import ProjectSerializer
from .serializers import ContributorSerializer
from .serializers import IssueSerializer

from .permissions import CanEditOrDestroyProject
from .permissions import CanAddContributorInProject
from .permissions import CanListContributorOfProject
from .permissions import CanDestroyContributorOfProject

from .permissions import IssueViewsetPermission


#
# 1. User registration - POST - /signup/
#
class SignupAPIView(APIView):  
    
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = SignupSerializer(data=user)

        if serializer.is_valid():
            serializer.save()
            return Response( {"User (serializer.data)" : serializer.data }, status=status.HTTP_201_CREATED )

        return Response( { "Errors" : serializer.errors }, status=status.HTTP_400_BAD_REQUEST )


# Endpoint :
#           /projects/
#           /projects/{id}
#
# 3. GET - Retrieve the list of all the projects attached to the connected user
# 4. POST - Create a project
# 5. GET - Retrieve project details from its id
# 6. PUT - Update a project
# 7. DELETE - Delete a project and its problems
#
class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, CanEditOrDestroyProject]
    
    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.filter(contributors=user) | Project.objects.filter(author=user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Endpoint :
#           /projects/{id}/users/
#           /projects/{id}/users/{id}
#
# 8.  POST - Add a collaborator to a project
# 9.  GET - Retrieve the list of all users attached to a project
# 10. DELETE - Remove a user from a project

class ProjectsUsersViewset(ModelViewSet):

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, CanAddContributorInProject, CanListContributorOfProject, CanDestroyContributorOfProject]


    def create(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')

        user_id = request.data.get('user_id')
        permissions = request.data.get('permissions')
        role = request.data.get('role')
     
        project = Project.objects.get(id=project_id)
        user = User.objects.get(id=user_id)

        contributor = Contributor(project=project, user=user, permissions=permissions, role=role)
        contributor.save()

        serializer = ContributorSerializer(contributor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        contributors = Contributor.objects.filter(project_id=project_id)
        serializer = ContributorSerializer(contributors, many=True)

        message = { "message" : "ProjectsUsersViewset - List", "data" : serializer.data}
        return Response(message, status=status.HTTP_200_OK)


    def destroy(self, request, *args, **kwargs):
        print("> ProjectsUsersViewset : destroy()")

        user_id = self.kwargs.get('pk')
        project_id = self.kwargs.get('project_id') 

        project = Project.objects.get(id=project_id)
        user = User.objects.get(id=user_id)

        contributor = Contributor.objects.filter(project=project, user=user)
        contributor.delete()

        return Response("", status=status.HTTP_204_NO_CONTENT)


# Endpoint :
#           /projects/{id}/issues/
#           /projects/{id}/issues/{id}
#
# 11. GET - Retrieve the list of problems related to a project
# 12. POST - Creating a problem in a project
# 13. PUT - Update a problem in a project
# 14. DELETE - Delete a problem from a project

class IssueViewset(ModelViewSet):

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IssueViewsetPermission]

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        queryset = Issue.objects.filter(project_id=project_id)
        return queryset

    def create(self, request, *args, **kwargs):      
        print("> IssueViewset: create()")

        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(id=project_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['project'] = project
        serializer.validated_data['assignee'] = request.user

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
        print("> IssueViewset: update()")

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

