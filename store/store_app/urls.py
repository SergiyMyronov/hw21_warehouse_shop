from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from . import views

urlpatterns = [
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('order/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('book/order/new/', views.OrderCreateView.as_view(), name='order_new'),
    path('order/edit/<int:pk>', views.OrderUpdateView.as_view(), name='order_form'),
    path('order/delete/<int:pk>', views.OrderDeleteView.as_view()),
    path('order/orderline/', views.OrderLineListView.as_view(), name='orderline_list'),
    path('order/orderline/new/', views.OrderLineCreateView.as_view(), name='orderline_form'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_done/', views.signup_done, name='signup_done'),
    path('user/', views.UserDetailView.as_view(), name='user_detail'),
    path('user/edit', views.UserUpdateView.as_view(), name='user_form'),
    path('', include('django.contrib.auth.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
