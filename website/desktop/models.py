# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Category(models.Model):
    category_text = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
    	return self.category_text

  


class Article(models.Model):
	category = models.ManyToManyField(Category)
	article_text = models.CharField(max_length=20000)
	pub_date = models.DateTimeField('date published')
	headline = models.CharField(max_length=200)
	article_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

	def __str__(self):              # __unicode__ on Python 2
		return self.headline