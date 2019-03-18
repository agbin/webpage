from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.base, name='details'),
    # path('comment/', views.CommentsList.as_view(), name='comments'),

    path('search/', views.search, name='search'),
    path('message/', views.message, name='message'),
    path('about/', views.about_us, name='about'),
    path('projects/', views.projects, name='projects'),
    path('offer/', views.offers, name='offer'),
    path('references/', views.reference, name='references'),
    path('details/<int:pk>/', views.Project_Detail.as_view(), name='project-details'),
    path('project/<int:pk>/edit/', views.ProjectUpdate.as_view(), name='project-update'),

    path('project/add/', views.ProjectCreate.as_view(), name='project-add'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

