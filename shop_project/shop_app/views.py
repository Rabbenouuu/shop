from django.shortcuts import render
from shop_app.models import Product, Client

def index(request):
	products = Product.objects.all()
	return render(request,'index.html',{'products':products})

def product(request, product_id):
	product = Product.objects.get(id=product_id)
	return render(request,'product.html',{'product':product})

def clients(request):
	clients = Client.objects.all()
	return render(request,'clients.html',{'clients':clients})

def client(request, client_id):
	client = Client.objects.get(id=client_id)
	products = Product.objects.all().filter(client=client_id)
	return render(request,'client.html',{'client':client, 'products':products})

