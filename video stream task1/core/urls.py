from django.urls import path
from core.views import SignUpView, ProfileView
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('create/', views.create_video, name='create_video'),
    path('edit_video/<int:pk>/', views.edit_video, name='edit_video'),
    path('video_list/', views.video_list, name='video_list'),
    path('delete_video/<int:pk>/', views.delete_video, name='delete_video'),
    path('stream_video/<int:pk>/', views.stream_video, name='stream_video'),
    path('api/videos/', views.api_videos, name='api_videos'),
    path('api/videos/<int:id>/', views.api_video_detail, name='api_video_detail'),
    path('video_search/', views.video_search, name='video_search'),



]