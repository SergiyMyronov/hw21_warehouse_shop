from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from store_app.forms import OrderForm
from store_app.models import Book, Order, OrderLine


def index(request):
    return HttpResponse("Hello, world. You're at the store_app index.")


@method_decorator(cache_page(5), name='dispatch')
class BookListView(ListView):
    model = Book
    fields = [
        'ISBN',
        'author_name',
        'title',
        'pages',
        'price',
        'pubdate',
        'quantity',
    ]
    paginate_by = 15


def order_cart(request):
    cart, created = Order.objects.get_or_create(
        customer_name=request.user.username,
        customer_mail=request.user.email,
        status='cart')
    order_lines = OrderLine.objects.filter(order=cart)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = OrderForm(instance=cart)

    return render(request, 'store_app/order_cart.html', {'form': form, 'order_id': cart.id, 'order_lines': order_lines})


class OrderListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Order
    fields = [
        'order_num',
        'order_date',
        'store_num',
        'store_name',
        'customer_name',
        'customer_mail',
        'status',
    ]
    success_url = reverse_lazy('order_list')
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(customer_name=self.request.user.username).exclude(status='cart')


class OrderDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Order
    fields = [
        'order_num',
        'order_date',
        'store_num',
        'store_name',
        'customer_name',
        'customer_mail',
        'status',
    ]
    success_url = reverse_lazy('order_detail')

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        order_lines = OrderLine.objects.filter(order_id=context['order'])
        context['order_lines'] = order_lines
        return context


class OrderCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Order
    fields = [
        'order_num',
        'order_date',
        'store_num',
        'store_name',
    ]
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.customer_name = self.request.user.username
        order.customer_mail = self.request.user.email
        order.status = 'cart'
        order.save()
        self.object = order
        return HttpResponseRedirect(self.get_success_url())


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Order
    fields = [
        'order_num',
        'order_date',
        'store_num',
        'store_name',
        'status',
    ]
    success_url = reverse_lazy('order_list')


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Order
    success_url = reverse_lazy('order_list')


class OrderLineCreateView(CreateView):
    model = OrderLine
    fields = [
        'book',
        'quantity',
    ]
    success_url = reverse_lazy('order_cart')

    def form_valid(self, form):
        ord_line = form.save(commit=False)
        ord_line.order_id = self.kwargs.get('pk')
        book = Book.objects.get(id=ord_line.book_id)
        ord_line.ISBN = book.ISBN
        ord_line.author_name = book.author_name
        ord_line.title = book.title
        ord_line.price = book.price
        ord_line.save()
        self.object = ord_line
        return HttpResponseRedirect(self.get_success_url())


class OrderLineUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = OrderLine
    fields = [
        'quantity',
    ]
    success_url = reverse_lazy('order_cart')


class OrderLineDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = OrderLine
    success_url = reverse_lazy('order_cart')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signup_done')
    template_name = 'registration/signup.html'


def signup_done(request):
    return render(request, 'registration/signup_done.html')


class UserDetailView(DetailView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


class UserUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    fields = ['email', 'first_name', 'last_name']
    success_url = reverse_lazy('book_list')

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
