from django.shortcuts import render
from django.shortcuts import redirect
from .models import requests, user_info, messages
from .forms import commentAdd, postForm

# Create your views here.
def index(request):
    posts = requests.objects.all()
    users = user_info.objects.all()
    header = ['ID','タイトル','目的地','出発地','日付','テキスト']
    my_dict2 = {
        'title':'タイトル',
        'posts': posts,
        'users': users,
        'header': header,
    }
    return render(request, 'main/index.html', my_dict2)

def post(request):
    message = ''
    if (request.method == 'POST'):
        form = postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/')
        else:
            message = '再入力して下さい'
    modelform_dict = {
        'title':'投稿画面',
        'form': postForm(),
        'message': message,
    }
    return render(request, 'main/post.html', modelform_dict)

def chat(request, num):
    message = ''
    chat_room = requests.objects.get(id=num)
    comment = messages.objects.all().filter(post_id=chat_room)
    if (request.method == 'POST'):
        form = commentAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/chat')
        else:
            message = '再入力して下さい'
    update_dict = {
        'title':'チャット画面',
        'id': num,
        'form': commentAdd(instance=chat_room),
        'comment': comment,
        'message': message,
    }
    return render(request, 'main/chat.html', update_dict)
