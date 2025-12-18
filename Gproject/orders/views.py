from django.shortcuts import render # type: ignore

# Create your views here.
def show_cart(request):
    return render(request,'cart.html')