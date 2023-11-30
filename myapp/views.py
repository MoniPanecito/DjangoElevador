from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import RetrieveAPIView
from .models import Project
from .serializers import ProjectSerializer

class LatestSensorDataView(RetrieveAPIView):
    serializer_class = ProjectSerializer

    def get_object(self):
        latest_data = Project.objects.latest('id')
        return latest_data

# Create your views here.
def index (request):
    return render(request,'index.html')
def hello(request,username):
    return HttpResponse("<h1>Hello %s</h1>"%username)
