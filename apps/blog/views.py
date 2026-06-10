from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Article
from .forms import CommentForm


def blog_list(request):
    articles = Article.objects.filter(is_published=True)
    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/list.html', {
        'page_obj': page_obj,
        'page_title': 'Blog — Stunt Bike Extreme Tips, Tricks & News',
        'meta_description': 'Read the latest tips, tricks, updates, and news about Stunt Bike Extreme on our blog.',
    })


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    comments = article.get_approved_comments()
    form = CommentForm()

    return render(request, 'blog/detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
        'page_title': article.effective_meta_title,
        'meta_description': article.effective_meta_description,
    })


def add_comment(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            messages.success(request, 'Your comment has been submitted and is awaiting moderation.')
        else:
            messages.error(request, 'Please correct the errors below.')
    return redirect('article_detail', slug=slug)
