from django.shortcuts import render


# Create your views here.

# 首页
def index(request):
    return render(request, 'lunious/index1.html')


# 首页_1
def index1(request):
    return render(request, 'lunious/index1.html')


# 首页_2
def index2(request):
    return render(request, 'lunious/index2.html')
