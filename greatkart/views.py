from csv import reader
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return reader(request, 'home.html', context=context)