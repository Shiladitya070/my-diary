"""MyDiary URL Configuration
Create Your Route Related to Notes Here
"""

from django.urls import path
from . import views

urlpatterns = [
    path("create",views.create,name='note-create'),
    path('edit/<int:id>',views.edit,name='note-edit'),
    path('show/<int:id>',views.show,name='note-delete'),
    path('delete/<int:id>',views.delete,name='note-delete'),
]
