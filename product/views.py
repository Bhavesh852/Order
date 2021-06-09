from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import *

def index(request):
	cust = Customer.objects.all()
	pro = Product.objects.all()
	context = {
		'customer' : cust,
		'product' : pro,
	}
	return render(request, 'product/index.html', context)

def order_form(request):
	if request.method == "POST":
		customer = request.POST['customer']
		product = request.POST['product']
		price = request.POST['price']
		qty = request.POST['qty']
		total = request.POST['total']

		c = Customer.objects.get(first_name=customer)
		p = Product.objects.get(name=product)
		myorder = Order(customer_id=c, product_id=p, unit_price=price, qty=qty, total_price=total)

		myorder.save()

		return redirect('/')


def list_page(request):
	o = Order.objects.all()
	return render(request, "product/list-page.html", {'order':o})


class SearchListView(ListView):
	model = Order
	template_name = 'product/search.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		query = self.request.GET.get('q', None)
		l1 = {}
		c = Customer.objects.all()
		if query is not None:
			if c.filter(first_name__icontains=query):
				name = c.filter(first_name__icontains=query)
				o=Order.objects.all()
				for i in range(len(name)):
					try:
						l1[i] = Order.objects.get(customer_id=name[i])
					except:
						pass
		context['order'] = l1
		
		return context


def edit(request, myid):
	if request.method == 'POST':
		order = Order.objects.get(id=myid)
		order.qty = request.POST['qty']
		order.total_price = request.POST['total']

		order.save()

		return redirect('/list-page/')
	else:
		order = Order.objects.get(id=myid)
		return render(request, 'product/edit.html', {'order':order})

def delete_order(request, myid):
	order = Order.objects.get(id=myid)
	order.delete()
	return redirect('/list-page/')