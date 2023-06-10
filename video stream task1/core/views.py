from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from core.forms import SignUpForm, ProfileForm,VideoForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from core.serializers import VideoSerializer
import cv2
from django.http import StreamingHttpResponse
from core.models import Video
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'

# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'commons/profile.html'

#video create
def create_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            print("vvvvvvvvvvvvvvvvvvvvvvvv",video)
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'commons/create_video.html', {'form': form})

#video search
def video_search(request):
    query = request.GET.get('query')
    videos = Video.objects.filter(name__icontains=query)
    return render(request, 'commons/video_list.html', {'videos': videos})

#All video get
def video_list(request):
    videos = Video.objects.all()    
    print("videosssssssssss",videos)
    return render(request, 'commons/video_list.html', {'videos': videos})

#id using edit video
def edit_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VideoForm(instance=video)
    return render(request, 'commons/edit_video.html', {'form': form, 'video': video})


#id video  deleted 

def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.delete()
    return redirect('home')

#id using video live stream 
def stream_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video_path = video.path
    print("video+pa000th",video_path)
    def video_stream():
        cap = cv2.VideoCapture(video_path)
        print("ccccccccccccccccc",cap)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            _, imgencode = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + imgencode.tobytes() + b'\r\n\r\n')

    return StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')


@api_view(['GET', 'POST'])
def api_videos(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


@api_view(['GET', 'PUT', 'DELETE'])
def api_video_detail(request, id):
    video = get_object_or_404(Video, pk=id)

    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        video.delete()
        return Response(status=204)
    
