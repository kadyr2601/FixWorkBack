from rest_framework import serializers
from . import models

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


class SEOSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SEO
        fields = '__all__'