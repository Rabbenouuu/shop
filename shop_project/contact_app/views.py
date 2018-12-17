from django.shortcuts import render, redirect
from contact_app.models import Contact
from contact_app.forms import ContactForm

def contact_form(request):
	if request.method == 'POST':
		subject = request.POST.get('subject')
		email = request.POST.get('email')
		text = request.POST.get('text')
		Contact.objects.get_or_create(subject=subject,email=email,text=text)[0]
		return redirect('contact_succes/')

	return render(request,'contact.html',{'contact_form':ContactForm()})

def contact_succes(request):
	return render(request,'contact_succes.html')


