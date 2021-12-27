from django.shortcuts import render

def index(requests):
    return render(requests,'website/index.html')

def about(requests):
    return render(requests,'website/about.html')

def contact(requests):
    return render(requests,'website/contact.html')

def pricing(requests):
    return render(requests,'website/pricing.html')

def faq(requests):
    return render(requests,'website/faq.html')

def blog_home(requests):
    return render(requests,'website/blog-home.html')

def blog_post(requests):
    return render(requests,'website/blog-post.html')

def portfolio_overview(requests):
    return render(requests,'website/portfolio-overview.html')

def portfolio_item(requests):
    return render(requests,'website/portfolio-item.html')
