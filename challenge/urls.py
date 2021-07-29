"""challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView, LogoutView
from rest_framework import routers

from apps.articles.api import views as article_views
from apps.authors.api import views as authors_views
from apps.categories.api import views as categories_views

router = routers.SimpleRouter()
router.register('articles', article_views.ArticlePublicViewSet, basename='article')
router.register('admin/categories', categories_views.CategoryViewSet, basename='category')
router.register('admin/authors', authors_views.AuthorViewSet, basename='author')
router.register('admin/articles', article_views.ArticleAdminViewSet, basename='admin_article')

api_views = router.urls + [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('sign-up/', RegisterView.as_view(), name='rest_register'),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_views)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
