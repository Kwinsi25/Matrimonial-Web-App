from django.urls import path
from . import api_views

urlpatterns = [
    path('profiles/', api_views.ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', api_views.ProfileDetail.as_view(), name='profile-detail'),
]
