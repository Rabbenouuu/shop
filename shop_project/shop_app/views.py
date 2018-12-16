from django.shortcuts import render
from shop_app.models import Product, Client, Comment
from shop_app.forms import CommentForm
import datetime


def index(request):
	products = Product.objects.all()[:20]
	return render(request,'index.html',{'products':products})

def product(request, product_id):
	product = Product.objects.get(id=product_id)
	comments = Comment.objects.all().filter(product_id=product_id)
	return render(request,'product.html',{'product':product,'comments':comments})

def clients(request):
	clients = Client.objects.all()
	return render(request,'clients.html',{'clients':clients})

def client(request, client_id):
	client = Client.objects.get(id=client_id)
	products = Product.objects.all().filter(client=client_id)
	return render(request,'client.html',{'client':client, 'products':products})

def comment_form(request,product_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		product = Product.objects.get(id=product_id)
		date = datetime.datetime.now()
		Comment.objects.get_or_create(username=username,text=text,date=date,product=product)[0]
		return render(request,'comment_form.html', {'comment_form':CommentForm() })
















