from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from news.models import Article
import json
import pytz
import datetime

def index(request):
	print "index"
	context = {}
	return render(request, 'news/index.html', context)
# Create your views here.

@csrf_exempt  
def edit(request):
	print "edit"
	context = {}
	return render(request, 'news/edit.html', context)

@csrf_exempt  
def list(request):
	print "list"
	context = {'articles': Article.objects.all(),}
	return render(request, 'news/article-list.html', context)

@csrf_exempt  
def add(request):
	print "add"
	title = request.REQUEST.get('title','')
	author = request.REQUEST.get('author', '')
	content = request.REQUEST.get('content', '')
	tz = pytz.timezone("US/Eastern")
	print title, author, content
	print tz.localize(datetime.datetime.now())
	tmp = Article(title=title, author=author, content=content, pub_date=tz.localize(datetime.datetime.now()))
	tmp.save()
	response = {}
	return HttpResponse(json.dumps(response), content_type='application/json')

@csrf_exempt  
def detail(request, news_id):
<<<<<<< HEAD
    	try:
        		print news_id
    	except Question.DoesNotExist:
        		raise Http404("Question does not exist")
    	return render(request, 'news/article.html', {'news_id': news_id})
=======
	print "detail"
	article = Article.objects.get(id = news_id)
	try:
		print news_id
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'news/article.html', {'article': article})

@csrf_exempt  
def delete(request):
	print "delete"
	article_id = request.REQUEST.get('article_id','')
	print type(article_id)
	a = Article.objects.get(id=int(str(article_id)))
	try:
		a.delete()
	except IOError as e:
    		print "I/O error({0}): {1}".format(e.errno, e.strerror)
	except ValueError:
    		print "Could not convert data to an integer."
	except:
    		print "Unexpected error:", sys.exc_info()[0]
	print "4"
	print "a"+str(a.id)+"a"
	print "title="+a.title
	print "content="+a.content
	return render(request, 'news/article.html', {})
>>>>>>> ef5a76cac83f9a03c24237ffec30fcacd97ffd72
