from rest_framework import serializers
from . import models


class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainBanner
        fields = '__all__'


class ProjectSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectSection
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    sections = ProjectSectionSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'


class ServiceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceCard
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'
        depth = 1


class PageBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PageBanner
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = '__all__'


class FeedbackFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = models.FeedbackFile
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    files = FeedbackFileSerializer(write_only=True)

    class Meta:
        model = models.Feedback
        fields = '__all__'

    def create(self, validated_data):
        files_data = validated_data.pop('files')
        feedback = models.Feedback.objects.create(**validated_data)
        for file_data in files_data:
            models.FeedbackFile.objects.create(feedback=feedback, **file_data)
        return feedback


class RestorationServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RestorationService
        fields = '__all__'


class RestorationSerializer(serializers.ModelSerializer):
    services = RestorationServiceSerializer(many=True, read_only=True)

    class Meta:
        model = models.Restoration
        fields = '__all__'
        depth = 1


class RestorationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restoration
        fields = ('id', 'name_ru', 'name_en', 'slug')