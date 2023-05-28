from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .serializers import SignupSerializer
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

#
# 1. User signup - POST - /signup/
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


#
# 3. Get the list of all projects attached to the logged in user (Contributor or Author)
#
# 4. Create a project (Author will be the authenticated user)
#
class ProjectListCreateAPIView(ListCreateAPIView):
    
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.filter(contributors=user) | Project.objects.filter(author=user)
        return queryset    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

