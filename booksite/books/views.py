from django.shortcuts import render
from django.views import generic, View 
from django.urls import reverse

from .form import BookForm
from .models import Books


class BooksListView(generic.ListView):
	template_name = 'books/index.html'
	context_object_name = 'books'
	latest_published_books = Books.objects.order_by('-published_date')[:10]

	def get_queryset(self):
		return self.latest_published_books


class BooksDetailView(generic.DetailView):
	template_name = 'books/detail.html'
	model = Books


class BooksAdd(generic.TemplateView):
	template_name = "books/bookadd.html"

	def post(self, request, *args, **kwargs):
		books_form = BookForm(request.POST)

		if books_form.is_valid():
			books_form.save()
			succeed = Ture 
			return HttpResponseRedirect(reverse('books: booklist'))
		else:
			succeed = "请正确填写信息"
			context = {
				'succeed':succeed,
				'form': books_form,
			}
			return render(request, self.template_name, context=context)

	def get(self, request, *args, **kwargs):
		books_form = BookForm()
		context = {
			'form': books_form,
		}
		return render(request, self.template_name, context=context)
    
