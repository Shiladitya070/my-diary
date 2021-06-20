"""MyDiary URL Configuration
Create Your Route Related to Notes Here
"""

from django.urls import path
from . import views

urlpatterns = [
    path("create",views.create,name='note-create'),
    path('edit/<slug:slug>',views.edit,name='note-edit'),
    path('show/<slug:slug>',views.show,name='note-show'),
    path('delete/<int:id>',views.delete,name='note-delete'),
    
]
