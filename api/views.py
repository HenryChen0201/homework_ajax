from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .models import Member
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

# Create your views here.
# /api/register?name=Tom&email=Tom@company.com&age=30
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Guest')
        email = request.POST.get('email', 'Guest@company.com')
        age_str = request.POST.get('age', 30)
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if not all([name, email, password, password1, age_str]):
            content = "請輸入所有資訊"
            return HttpResponse(content, 'text/plain')
        
        if Member.objects.filter(user_name=name).exists():
            content = "帳號已存在"
            return HttpResponse(content, 'text/plain')

        if Member.objects.filter(user_email=email).exists():
            content = "郵箱已被註冊"
            return HttpResponse(content, 'text/plain')

        if password != password1:
            content = "密碼不一致"
            return HttpResponse(content, 'text/plain')

        try:
            age = int(age_str)
        except (ValueError, TypeError):
            return HttpResponse("年紀請輸入數字", 'text/plain')

        if age <= 0:
            return HttpResponse("年紀必須大於0", 'text/plain')

    #  接收傳過來的檔案
        avatar = request.FILES.get('avatar')
        file_name = avatar.name
    #    把檔案寫進uploads資料夾
        if avatar:
            fs = FileSystemStorage()
            upload_file = fs.save(file_name, avatar)

        Member.objects.create(
            user_name = name,
            user_password = make_password(password), 
            user_age = age,
            user_email = email,
            user_avatar = upload_file,
            last_update=datetime.now()
        )
        content = "註冊成功"
        return HttpResponse(content, 'text/plain')
        
def check_name(request, name):
    # filter(name=name).exists()
    request.GET.get(name)
    memName = Member.objects.filter(user_name=name).exists()
    if memName:
        content = "帳號已存在"
    else:
        content = "帳號可使用"

    return HttpResponse(content, content_type='text/plain; charset=utf-8')