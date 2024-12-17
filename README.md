###API to allow admin users to view and edit the users and groups in the system.###

set up: ==> Virtual Environment
        ==> pip install django djangorestframework
        ==> Project
        ==> App
        ==> Migrate
        ==> CreateSuperUser
        ==> Settings.py  add app & rest_framework in Installed Apps

In app, add serializers.py, then:
                            from django.contrib.auth.models import Group, User
                            from rest_framework import serializers


                           class UserSerializer(serializers.HyperlinkedModelSerializer):
                                 class Meta:
                                     model = User
                                     fields = ['url', 'username', 'email', 'groups']


                           class GroupSerializer(serializers.HyperlinkedModelSerializer):
                                class Meta:
                                     model = Group
                                     fields = ['url', 'name']

in app, views.py, then:

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
                                     
in app, urls.py, then:
from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


in settings.py add pagination:
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


python manage.py runserver
