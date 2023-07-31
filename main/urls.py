
from django.urls import path
from . import views 
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),
    path('task/create',views.TaskCreateView.as_view(), name = 'task_create'),
    path('task/<pk>',views.TaskVeiw.as_view(), name = 'task_detail'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    

]