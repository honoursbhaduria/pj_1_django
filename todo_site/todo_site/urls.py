
# from django.contrib import admin 
# from django.urls import path
# from django.contrib import admin
# from django.urls import include, path


# urlpatterns = [
#     path('' , include('todo.urls')), 
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]
