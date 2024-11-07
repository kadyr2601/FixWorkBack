from rest_framework import views, response
from . import models, serializers


class ProjectsPageView(views.APIView):
    def get(self, request):
        project_list = models.Project.objects.all()
        projects_page = models.ProjectsPage.objects.first()

        projects_page_serializer = serializers.ProjectPageSerializer(projects_page, context={'request': request})
        project_list_serializer = serializers.ProjectSerializer(project_list, many=True, context={'request': request})

        data = projects_page_serializer.data
        data['project_list'] = project_list_serializer.data
        return response.Response(data)
