from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()

            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)


@login_required
def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()

    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'detail.html', context)

def comment_create(request, article_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)

        # comment.user = request.user
        # article = Article.objects.get(id=article_id)
        # comment.article = article

        comment.user_id = request.user.id
        comment.article_id = article_id

        comment.save()

        return redirect('articles:detail', id=article_id)

def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    if request.user == comment.user:
        comment.delete()
    

    return redirect('articles:detail', id=article_id)