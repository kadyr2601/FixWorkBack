from rest_framework import serializers
from . import models

class ProjectSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectSection
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    sections = ProjectSectionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = '__all__'


class ProjectPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectsPage
        fields = '__all__'
        depth = 1