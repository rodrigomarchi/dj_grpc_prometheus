from django.contrib import admin
from django.urls import path, include

from caller.views import reverse_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proxy/<str:name>/', reverse_name, name='proxy_grpc'),
    path('prometheus/', include('django_prometheus.urls')),

]
