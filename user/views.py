# coding = utf-8
from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1
from django.http import HttpResponseRedirect


# Create your views here.

# 注册页面
def register(request):
    return render(request, 'user/register.html')


def register_handle(request):
    # 接收注册信息
    post = request.POST
    uname = post.get('user_name')
    upwd1 = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码是否相等
    if upwd1 != upwd2:  # 两次密码不一致
        return redirect('user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(upwd1.encode("latin1"))
    upwd = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uemail = uemail
    user.save()
    # 注册成功，转到登录页面
    return redirect('/user/login/')


# 登录页面
def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'user/login.html', context)


def login_handle(request):
    # 接收登录信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)
    # 根据用户名查询对象
    users = UserInfo.objects.filter(uname=uname)
    # 判断：如果未查看则用户名错误，如果查看则判断密码是否正确，正确则跳转到用户中心
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode("latin1"))
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = users[0].uname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'user/login.html', context)


# 用户中心
def info(request):
    users = UserInfo.objects.filter(id=request.session['user_id'])[0]
    user_email = users.uemail
    context = {'title': '用户中心', 'user_email': user_email, 'user_name': request.session['user_name']}
    return render(request, 'user/user_center_info.html', context)
