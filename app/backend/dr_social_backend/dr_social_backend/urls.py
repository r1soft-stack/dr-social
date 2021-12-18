"""dr_social_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.models import User
from django.urls import path, include

from rest_framework import routers
from rest_framework import generics, permissions, serializers
from rest_framework.documentation import include_docs_urls

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from . import views

handler404 = 'dr_social_backend.views.not_found'
handler500 = 'dr_social_backend.views.server_error'
handler403 = 'dr_social_backend.views.not_found'
handler400 = 'dr_social_backend.views.not_found'


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


api_v1 = [
    path('docs/', include_docs_urls(public=False, title='Ristrutturatori planetari',
                                        description='API Galattiche')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/v1/', include(api_v1)),
    path('', views.index, name='index')
]
