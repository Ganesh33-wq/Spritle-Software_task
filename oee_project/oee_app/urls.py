from django.urls import path, include
from oee_app.views import oee_data
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/oee/', oee_data, name='oee-data'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
