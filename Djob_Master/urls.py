"""Djob_Master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import debug_toolbar
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from Djob_Master import settings
from apis.views import FacebookLogin, TwitterLogin

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("account/", include("allauth.urls")),
    path("profile/", include("djob_profile.urls")),
    path("jobs/", include("djob_jobs.urls")),
    # path('rts/', include('random_tester.urls')),
    # Ckeditor
    url(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
    
    # APIS
    path("api/v1/", include("apis.urls")),
    path(
        "swagger<str>:format",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "docs/api/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),

    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('auth/twitter/', TwitterLogin.as_view(), name='twitter_login')





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
