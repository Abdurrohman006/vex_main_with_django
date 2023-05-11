from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index, name='index'),
    path('products/',  views.products, name='products'),
    path('product_details/<str:p_id>',  views.productDetails, name='product_details'),
    path('blog/',  views.blog, name='blog'),
    path('blog_details/',  views.blogDetails, name='blog_details'),
    path('contact/',  views.contact, name='contact'),
    path('privacy_policy/',  views.privacyPolicy, name='privacy_policy'),
    path('terms_conditions/',  views.termsConditions, name='terms_conditions'),
]
