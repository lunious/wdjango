from django.shortcuts import render


# Create your views here.

# 首页_1
def index(request):
    return render(request, 'lunious/index.html')
# 首页_1
def index_1(request):
    return render(request, 'lunious/index_1.html')

# 首页_2
def index_2(request):
    return render(request, 'lunious/index_2.html')

