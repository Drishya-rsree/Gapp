from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def list_products(request):
    """_Summary
   returns products list page
   Args:
   request (_type_): _descriptio
   
   
   
    
    :param request: Description
    """
    return render(request,'products_layout.html')
def detail_product(request):
    return render(request,'product_detail.html')
