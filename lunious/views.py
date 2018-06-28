from django.shortcuts import render


# Create your views here.
# 首页_1
def index_1(request):
    return render(request, 'lunious/index_1.html')
