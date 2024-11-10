#To entering CharField
from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'full_name', 'age', 'qualification', 'current_salary', 'expected_salary', 'role']
