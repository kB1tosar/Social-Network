from django.urls import path
from v1.apps.user_account.views import *

app_name = 'profile'
urlpatterns = [
    path('profile/create/', ProfileCreateView.as_view()),
    path('profile/all/', ProfileListView.as_view()),
    path(
        'profile/detail/<int:pk>/',
        ProfileDetailView.as_view(),
    ),
]