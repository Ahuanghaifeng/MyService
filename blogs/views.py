#encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import sys
import json
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')


# 参考方法2：增加了日期类型判断
def convert_obj_to_dicts(model_obj):
    object_array = []
    for obj in model_obj:
        # 获取到所有属性
        # field_names_list = obj._meta.fields
        fields = []
        for field in obj._meta.fields:
            fields.append(field.name)

        for fieldName in fields:
            print fieldName
            try:
                fieldValue = getattr(obj, fieldName)  # 获取属性值
                print type(fieldValue)
                if type(fieldValue) is datetime.date or type(fieldValue) is datetime.datetime:
                    #                     fieldValue = fieldValue.isoformat()
                    fieldValue = datetime.datetime.strftime(fieldValue, '%Y-%m-%d %H:%M:%S')
                    # 没想好外键与cache字段的解决办法
                #                 if hasattr(fieldValue, "__dict__"):
                #                     fieldValue = convert_obj_to_dicts(model_obj)
                setattr(obj, fieldName, fieldValue)
            # print fieldName, "\t", fieldValue
            except Exception, ex:
                print ex
                pass
                # 先把Object对象转换成Dict
        dict = {}
        dict.update(obj.__dict__)
        dict.pop("_state", None)  # 此处删除了model对象多余的字段
        object_array.append(dict)
    return object_array

def blog_index(request):
    # pk 是Primary key主键的意思即为文章id
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/article_page.html", {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, "blog/edit_page.html")
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, "blog/article_page.html", {'article': article})

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/html/index.html', {'articles': articles})

def main(request):
    articles = models.Article.objects.all()
    return render(request,'main.html',{'articles':articles})


def api_getAll_article(request):
    articles = models.Article.objects.all()
    json_data = convert_obj_to_dicts(articles)
    return HttpResponse(json.dumps(json_data), content_type="application/json")

