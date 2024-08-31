"""
URL configuration for onedeliveryback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework.response import Response
from rest_framework.views import APIView

class APIRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'fooditems': request.build_absolute_uri('/fooditems/'),
            'fooditem-detail': request.build_absolute_uri('/fooditems/<int:pk>/'),
            'orders': request.build_absolute_uri('/orders/'),
            'register': request.build_absolute_uri('/register/'),
            'login': request.build_absolute_uri('/login/'),
            'logout': request.build_absolute_uri('/logout/'),
        })

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api/', include('foodItem.urls')),
    path('api/', include('order.urls')),
]
