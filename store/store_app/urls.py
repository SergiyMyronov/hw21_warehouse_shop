from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from . import views

urlpatterns = [
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/cart', views.order_cart, name='order_cart'),
    path('book/order/new/', views.OrderDetailView.as_view(), name='order_new'),
    path('order/edit/<int:pk>', views.OrderUpdateView.as_view(), name='order_form'),
    path('order/delete/<int:pk>', views.OrderDeleteView.as_view()),
    path('order/orderline/new/<int:pk>', views.OrderLineCreateView.as_view(), name='orderline_new'),
    path('order/orderline/edit/<int:pk>', views.OrderLineUpdateView.as_view(), name='orderline_form'),
    path('order/orderline/delete/<int:pk>', views.OrderLineDeleteView.as_view()),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_done/', views.signup_done, name='signup_done'),
    path('user/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/edit', views.UserUpdateView.as_view(), name='user_form'),
    path('', include('django.contrib.auth.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
