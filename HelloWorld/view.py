from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'HelloWorld/shouye.html',{'hello':'测试网页看到说明成功',
                                                    'list1':'qqqqqqqqqqqq'})