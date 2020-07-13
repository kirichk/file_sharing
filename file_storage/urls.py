from django.urls import path
from . import views

app_name = 'file_storage'

urlpatterns = [
    path('', views.CreateFile.as_view(),name='upload'),
    path('all/', views.FileList.as_view(),name='all'),
    path('all/<slug:slug>/',views.FileDetail.as_view(),name="detail"),
]
