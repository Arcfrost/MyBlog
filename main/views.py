from django.http import Http404
from django.shortcuts import render,get_object_or_404

from main import models
# Create your views here.

def index(request):

    latest_posts=models.Article.objects \
        .all() \
        .order_by('-createdAt')[:10]

    context={
        "latest_posts": latest_posts,
    }
    return render(request,'main/index.html',context)


# def navbar(request):
#     latest_posts=models.Article.objects \
#         .all() \
#         .order_by('-createdAt')[:10]

#     context={
#         "latest_posts": latest_posts,
#     }
#     return render(request,'main/base.html',context)

def article(request,pk):

    # try:
    #     article=models.Article.objects.get(pk=pk)
    # except:
    #     raise Http404()

    article=get_object_or_404(models.Article,pk=pk)

    context={
        'article':article,
    }

    return render(request, 'main/article.html',context)

def author(request,pk):
    author=get_object_or_404(models.Author,pk=pk)
    latest_posts=models.Article.objects \
        .all() \
        .order_by('-createdAt')
    context={
        'author':author,
        "latest_posts": latest_posts

    }
    return render(request,'main/author.html',context)

def create_article(request):

    authors=models.Author.objects.all()
    
    context={
        'authors':authors
    }
    if request.method=="POST":
        article_data={
            "title":request.POST['title'],
            "content":request.POST['content']
        }
        article = models.Article.objects.create(**article_data)

        # author = models.Author.objects.get(pk=request.POST['author'])
        # article.authors.set([author])

        author = models.Author.objects.filter(pk=request.POST['author'])
        article.authors.set(author)
        context["success"]=True
    

    return render(request,'main/create_article.html',context)

def authors(request):
    
    authors=models.Author.objects.all()
    
    context={
        'authors':authors
    }


    return render(request,'main/authors.html',context)

def apply(request):

    context={}

    if request.method=="POST":
        author_data={
            "name":request.POST['name'],
        }
        author = models.Author.objects.create(**author_data)

        # author = models.Author.objects.get(pk=request.POST['author'])
        # article.authors.set([author])

        
        context["applied"]=True

    return render(request,'main/apply.html',context)