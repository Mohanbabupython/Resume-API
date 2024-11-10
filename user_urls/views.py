
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Resume
from .serializers import ResumeSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()  # Query all resumes
    serializer_class = ResumeSerializer  # Use the ResumeSerializer to format data
    permission_classes = [IsAuthenticated]  # authenticated users can access
