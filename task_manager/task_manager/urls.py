from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task-manager/', include('task_manager_app.urls')),
    path('', include('users.urls'))

]
