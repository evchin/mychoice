from django.urls import path
from . import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('vote/<str:pk>', views.vote, name='vote'),

    path('elections/', views.electionList, name='election-list'),
    path('elections/create/', views.electionCreate, name='election-create'),
    path('elections/detail/<str:pk>/', views.electionDetail, name='election-detail'),
    path('elections/update/<str:pk>/', views.electionUpdate, name='election-update'),
    path('elections/delete/<str:pk>/', views.electionDelete, name='election-delete'),
    path('elections/positions/<str:pk>/', views.electionPositionList, name='election-position-list'),

    path('positions/', views.positionList, name='position-list'),
    path('positions/create/', views.positionCreate, name='position-create'),
    path('positions/detail/<str:pk>', views.positionDetail, name='position-detail'),
    path('positions/update/<str:pk>', views.positionUpdate, name='position-update'),
    path('positions/delete/<str:pk>', views.positionDelete, name='position-delete'),
    path('positions/candidates/<str:pk>/', views.positionCandidateList, name='position-candidate-list'),

    path('candidates/', views.candidateList, name='candidate-list'),
    path('candidates/create/', views.candidateCreate, name='candidate-create'),
    path('candidates/detail/<str:pk>/', views.candidateDetail, name='candidate-detail'),
    path('candidates/update/<str:pk>', views.candidateUpdate, name='candidate-update'),
    path('candidates/delete/<str:pk>', views.candidateDelete, name='candidate-delete'),

    path('users/', views.userList, name='user-list'),
    path('users/update/', views.userUpdate, name='user-update'),
    path('users/detail/', views.userDetail, name='user-detail'),
    path('users/delete/', views.userDelete, name='user-delete'),

    path('openapi', get_schema_view(
        title="My Choice API",
        description="API Documentation",
        version="1.0.0"
    ), name='openapi-schema'),

    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]