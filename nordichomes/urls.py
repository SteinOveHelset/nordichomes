from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from cart.views import add_to_cart
from core.views import frontpage, shop, signup, login
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
