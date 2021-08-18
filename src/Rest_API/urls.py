from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from core.views import TestView, BooksView, BooksCreateView, BooksListCreateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='obtain-token'),

    path('method_1/', TestView.as_view(), name='method-1'),
    path('method_2/', BooksView.as_view(), name='method-2'),
    path('method_3/', BooksCreateView.as_view(), name='method-3'),
    path('method_4/', BooksListCreateView.as_view(), name='method-4'),
    
]