from django.urls import path
from . import views

urlpatterns=[
    path('note/',views.NoteViewSet.as_view(),name="Note"),
    path('note/<int:id>/',views.NoteVeiwDetials.as_view(),name="Note")
]