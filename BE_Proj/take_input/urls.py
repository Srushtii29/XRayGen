from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.select_document_type, name='select_document_type'),
    path('upload_broken_bones/', views.upload_broken_bones, name='upload_broken_bones'),
    # path('report/', views.view_report, name='view_report')
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
