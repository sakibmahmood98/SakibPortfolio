
from contents import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('certification/<int:pk>/', views.certification, name='certification'),
    path('project-document/<int:pk>/', views.project_document, name='project_document'),
    path('resume/<int:pk>/', views.resume, name='resume'),
    path('seminar/<int:pk>/', views.seminar, name='seminar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
