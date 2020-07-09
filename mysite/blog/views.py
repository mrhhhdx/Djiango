from django.shortcuts import render
from blog import models
# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello, World')


def hello2(request, year):
    return HttpResponse('Hello, World %s' % year)


def page(request, num=1):
    return HttpResponse(num)


# 下面的代码是新增加的，这个函数主要是把查询的内容渲染到 index.html页面去
def index(request):
    blog_index = models.Article.objects.all().order_by('-id')  # 从数据库中取出文章数据
    print(request.body)
    # 获取请求ip
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP
    print(ip)

    context = {
        'blog_index': blog_index,  # 将数据保存在blog_index
    }
    return render(request, 'index.html', context)  # 通过render进行模板渲染
