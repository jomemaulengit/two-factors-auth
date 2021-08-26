from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from tokenCreationEP.views import catch_id
from tokenValidationEP.views import validate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/get', catch_id),
    path('API/validate', validate),
]
