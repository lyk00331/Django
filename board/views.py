from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from django.urls import reverse
from django.utils import timezone

# Create your views here.
def index(request):
    boards = Post.objects.all().order_by('-time')
    return render(request, 'board/index.html', {'board': boards})


def create(request):
    boards = Post()
    if request.method == "POST":
        if request.POST['writer'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            boards.writer = request.POST['writer']
            boards.title = request.POST['title']
            boards.content = request.POST['content']
            boards.password = request.POST['password']
            boards.save()
            return redirect(f'/board/{ boards.id }')
        else:
            raise Http404("칸을 모두 채워주세요! 뒤로가기를 누르면 작성한 글이 유지된 상태로 이어 쓸 수 있습니다.")
    else:
        return render(request, 'board/create.html')


def read(request, id):
    try:
        boards = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'board/read.html', {'board': boards})


def update(request, id):
    boards = Post.objects.get(pk=id)
    if request.method == "POST":
        if request.POST['password'] == boards.password:
            if request.POST['title'] != '' and request.POST['content'] != '':
                boards.title = request.POST['title']
                boards.content = request.POST['content']
                boards.save()
                return redirect(f'/board/{ boards.id }')
            else:
                print("마찬가지로 채우지 않은 영역에 내용을 채워달라는 알림창을 띄워줌.")
        else:
            print("비밀번호를 확인해달라는 알림창을 띄워줌.")
    return render(request, 'board/update.html', {'board': boards})


def delete(request, id):
    boards = Post.objects.get(pk=id)
    if request.method == "POST":
        if request.POST['password'] == boards.password:
            boards.delete()
            return redirect('/board/')
        else:
            print("비밀번호를 확인해달라는 알림창을 띄워줌.")
    return render(request, 'board/delete.html', {'board': boards})