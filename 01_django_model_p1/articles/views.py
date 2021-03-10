from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

# 폼으로 받은 정보로 create하고 정보 넘겨주기
def create(request):
    data = request.GET
    title = data.get('title')
    content = data.get('content')
    
    article = Article.objects.create(title=title, content=content)
    context = {
        'article': article,
    }
    return render(request, 'articles/create.html', context)

# 받은 pk 값으로 레코드 정보 가지고 오기
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)