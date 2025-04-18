from django.urls import path
from . import views


urlpatterns = [
    path('user/',views.userView.as_view(),name='create user'),
]