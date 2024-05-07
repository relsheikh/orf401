from django.urls import path # type: ignore

from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('create/', views.create, name='create'),
    path('ai_interaction', views.transformers, name='ai_interaction'),

]
