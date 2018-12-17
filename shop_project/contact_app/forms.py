from django import forms
from contact_app.models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['subject','email','text']
		widgets = {
		'subject':forms.TextInput(attrs={
			'id':'contact-subject',
			'placeholder':'subject',
			'required':True
			}),
		'email':forms.EmailInput(attrs={
			'id':'contact-email',
			'placeholder':'Whrite a contact here ...',
			'required':True
			}),
		'text':forms.Textarea(attrs={
			'id':'contact-text',
			'placeholder':'Whrite a contact here ...',
			'required':True
			}),
		}