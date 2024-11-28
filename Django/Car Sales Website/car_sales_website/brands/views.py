from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import BrandForm
from .models import Brand

class AddBrand(CreateView):
    form_class= BrandForm
    model = Brand
    template_name = 'add_brand.html'
    success_url = reverse_lazy('homepage')
