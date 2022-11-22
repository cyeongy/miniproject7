from . import views
from django.urls import path

app_name = 'ML'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    # path('new/', views.ml_model_create, name='create'),
    # path('list', views.list, name='list'),
]
