from django.shortcuts import render, redirect
from shop_app.models import Product, Client, Comment, Question, Response
from shop_app.forms import CommentForm, QuestionForm, ResponseForm

import datetime


def index(request):
	products = Product.objects.all()[:20]
	return render(request,'index.html',{'products':products})


def product(request, product_id):
  product = Product.objects.get(id=product_id)
  comments = Comment.objects.all().filter(product_id=product_id)
  questions = Question.objects.all().filter(product_id=product_id)

  questions_with_responses = []
  for question in questions:
    question_with_responses = {
      'question': question,
      'responses': Response.objects.all().filter(question_id=question.id)
    }

    questions_with_responses.append(question_with_responses)

  return render(request, 'product.html', context={
      'product': product,
      'comments': comments,
      'questions': questions_with_responses,
    })


def clients(request):
	clients = Client.objects.all()
	return render(request,'clients.html',{'clients':clients})

def client(request, client_id):
	client = Client.objects.get(id=client_id)
	products = Product.objects.all().filter(id=client_id)
	return render(request,'client.html',{'client':client, 'products':products})

def comment_form(request, product_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		product = Product.objects.get(id=product_id)
		date = datetime.datetime.now()
		Comment.objects.get_or_create(username=username,text=text,date=date,product=product)
	return render(request,'comment_form.html', {'comment_form':CommentForm() })

def question_form(request, product_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		title = request.POST.get('title')
		text = request.POST.get('text')
		product = Product.objects.get(id=product_id)
		Question.objects.get_or_create(username=username,title=title,text=text,product=product)
		return redirect('/shop_app/products/{}'.format(product_id))

	return render(request,'question_form.html', {'question_form':QuestionForm() })

def response_form(request, question_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		question = Question.objects.get(id=question_id)
		Response.objects.get_or_create(username=username,text=text,question=question)
		return redirect('/shop_app/products/{}'.format(question.product.id))

	return render(request,'response_form.html',{'response_form':ResponseForm() })












