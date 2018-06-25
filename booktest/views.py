from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    booklist = BookInfo.books2.all()
    context = {'list': booklist}
    return render(request, 'booktest/index.html', context)


def show(request, id):
    book = BookInfo.books2.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'list': herolist}
    return render(request, 'booktest/show.html', context)


# 展示链接的页面
def getTest1(request):
    return render(request, 'booktest/getTest1.html')


# 接收一键一值得情况
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a': a1, 'b': b1, 'c': c1}
    return render(request, 'booktest/getTest2.html', context)


# 接收一键多值得情况
def getTest3(request):
    a1 = request.GET.getlist('a')
    context = {'a': a1}
    return render(request, 'booktest/getTest3.html', context)


def postTest1(request):
    return render(request, 'booktest/postTest1.html')


def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby}
    return render(request, 'booktest/postTest2.html', context)


# cookie练习
def cookieTest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if cookie.get('t1'):
        response.write(cookie['t1'])
    # response.set_cookie('t1', 'abc')
    return response


# 转向练习
def redTest1(request):
    # return HttpResponseRedirect('/redTest2')
    return redirect('/redTest2')


def redTest2(request):
    return HttpResponse('这是转向来的页面')


# 通过用户登录练血session
def session1(request):
    uname = request.session.get('myname', '未登录')
    context = {'uname': uname}
    return render(request, 'booktest/session1.html', context)


def session2(request):
    return render(request, 'booktest/session2.html')


def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    request.session.set_expiry(0)
    return redirect('/session1')


# 删除session
def session3(request):
    del request.session['myname']
    return redirect('/session1')
