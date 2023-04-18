"""drfsite URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from fitnes.views import *
from women.views import *
from rest_framework import  routers
from .routers import MyCustomRouter

# router = MyCustomRouter()
# router = routers.DefaultRouter()

# router.register(r'women', WomenViewSet, basename='women')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/', include(router.urls)), # api/v1/women/
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    # djoser
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # JWT
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # fitnes
    path('api/v1/fitnes/session/', SessionAPIList.as_view()),
    path('api/v1/fitnes/session/<int:pk>/', SessionAPIDetail.as_view()),
    path('api/v1/fitnes/cat-direction/', CatDirectionAPIList.as_view()),
    path('api/v1/fitnes/cat-direction/<int:pk>/', CatDirectionAPIDetail.as_view()),
    path('api/v1/fitnes/cat-coach/', CatCoachDirectionAPIList.as_view()),
    path('api/v1/fitnes/cat-coach/<int:pk>/', CatCoachDirectionAPIDetail.as_view()),
    path('api/v1/fitnes/cat-session/', CatSessionAPIList.as_view()),
    path('api/v1/fitnes/cat-session/<int:pk>/', CatSessionAPIDetail.as_view()),
    path('api/v1/fitnes/for-board/', SessionsForBoardAPIList.as_view()),
]
