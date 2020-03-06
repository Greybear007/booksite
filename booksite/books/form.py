from django import forms 

from .models import Books


class BookForm(forms.ModelForm):
	class Meta:
		model = Books
		fields = ['name', 'author', 'translator', 'publisher', 'published_date', 'category', 'pic', 'interduction']

