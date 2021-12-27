from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('pricing.html', views.pricing, name='pricing'),
    path('faq.html', views.faq, name='faq'),
    path('blog-home.html', views.blog_home, name='blog-home'),
    path('blog-post.html', views.blog_post, name='blog-post'),
    path('portfolio-overview.html', views.portfolio_overview, name='portfolio-overview'),
    path('portfolio-item.html', views.portfolio_item, name='portfolio-item'),
    
]
