"""portfolio_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from api.resources import ProjectResource, NoteResource
from tastypie.api import Api

# project_resource = ProjectResource()

#this creates the api
v1_api = Api(api_name='v1')
v1_api.register(ProjectResource()) # added project resource to v1 api
v1_api.register(NoteResource()) # added project resource to v1 api

urlpatterns = [
    # path('admin/', admin.site.urls),
    # include every v1 api url
    # when you hit a /api route, the only routes available are those listed in v1_api.urls
    url(r'^api/', include(v1_api.urls))
]
