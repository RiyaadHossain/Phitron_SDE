from django.shortcuts import render, redirect
from .models import Car
from comments.models import Comment
from order_histories.models import OrderHistory
from comments.forms import CommentForm
from django.views.generic import ListView
from brands.models import Brand

class CarListingView(ListView):
    model = Car
    template_name = 'car_listing.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        print(Brand.objects.all())
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        brand_id = self.request.GET.get('brand_id')
        if brand_id:
            queryset = queryset.filter(brand_id=brand_id)
        return queryset

def car_details(req, id):
    car = Car.objects.get(pk = id)
    form = CommentForm()
    comments = Comment.objects.filter(car=car)

    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('car_details', id=id)
    
    return render(req, 'car_details.html', {'car':car, 'form': form, 'comments': comments})

def buy_car(req, car_id):
    car = Car.objects.get(id=car_id)

    order = OrderHistory(car=car, user=req.user)
    order.save()

    car.quantity-=1
    car.save()

    return redirect('order_history_page')
    
