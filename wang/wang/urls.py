from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('wang_page/', include('wang_page.urls')),
    path('admin/', admin.site.urls),
]