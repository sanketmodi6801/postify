from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('posts/<str:pk>', views.posts, name='post'),
    path('search', views.search, name='search')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
