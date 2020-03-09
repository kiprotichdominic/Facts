from django.urls import path
from . import views
from .views import InvoiceCreateView

urlpatterns = [
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('invoice/', InvoiceCreateView.as_view(), name='invoice_upload')
    # path('products/', views.products, name='products'),
    # path('customer/<str:pk_test>/', views.customer, name="customer"),

    # path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]