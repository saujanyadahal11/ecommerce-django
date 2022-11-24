from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views
urlpatterns = [
    # path('', views.home),
    path('',views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('gender/<slug:data>', views.gender, name='gender'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('checkout/', views.checkout, name='checkout'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('addCategory/', views.addCategory, name='addCategory'),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
