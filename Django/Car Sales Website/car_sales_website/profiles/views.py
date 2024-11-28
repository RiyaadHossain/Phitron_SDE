from django.shortcuts import render
from .forms import CustomUserChangeForm
from django.shortcuts import redirect
from order_histories.models import OrderHistory

def my_profile(req):
    print("hello")
    return render(req, "my_profile.html")

def update_info(req):
    if req.method == 'POST':
        form = CustomUserChangeForm(instance= req.user,data=req.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_page') 
    else:
        form = CustomUserChangeForm(instance= req.user)

    return render(req, 'update_info.html', {'form': form})

def order_history(req):
    orders = OrderHistory.objects.filter(user=req.user)
    return render(req, 'order_history.html', {'orders':orders})