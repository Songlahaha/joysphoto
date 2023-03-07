from django.shortcuts import render, redirect
from .models import Slide, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.db.models import Q

# Create your views here.


def index(request):
    slides = Slide.objects.all()
    return render(request, 'index.html', {'slides':slides})



def about(request):
    return render(request, 'about.html')



def details(request):
    items = Post.objects.all()
    paginator = Paginator(items, 9)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)            #取得當前的頁數
    except PageNotAnInteger:        
        items = paginator.page(1)               #設定顯示第一頁
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'details.html', {'items':items})


def search_post(request):
    items = Post.objects.all()

    q = request.GET.get('q', None)
    if q:
        items = items.filter(Q(title__contains=q)|Q(location__contains=q))
    else:
        return redirect(reverse('details'))

    paginator = Paginator(items, 9)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)            #取得當前的頁數
    except PageNotAnInteger:        
        items = paginator.page(1)               #設定顯示第一頁
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'searchpost.html', {'items':items})



