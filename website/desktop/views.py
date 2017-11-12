# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Category, Article
from django.http import Http404


def index(request):
	categ_list = Category.objects.all()
	context = {'category_list': categ_list, 'articles_list': Category.objects.get(pk=6).article_set.order_by('-pub_date')[:4], 
	'tech_list': Category.objects.get(category_text="TECH").article_set.order_by('-pub_date')[:4], 'business_list': Category.objects.get(category_text="BUSINESS").article_set.order_by('-pub_date')[:4], 
	'fashion_list': Category.objects.get(category_text="FASHION").article_set.order_by('-pub_date')[:4], 'sports_list': Category.objects.get(category_text="SPORTS").article_set.order_by('-pub_date')[:4], 
	'politics_list': Category.objects.get(category_text="POLITICS").article_set.order_by('-pub_date')[:4], 'national_list': Category.objects.get(category_text="NATIONAL").article_set.order_by('-pub_date')[:4],
	'international_list': Category.objects.get(category_text="INTERNATIONAL").article_set.order_by('-pub_date')[:3]}
	return render(request, 'desktop/index.html', context)

# Create your views here.

def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        categ_list = Category.objects.all()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'desktop/page.html', {'article': article, 'category_list': categ_list})
