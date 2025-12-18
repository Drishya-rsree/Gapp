from django.shortcuts import render # type: ignore

# Create your views here.
def show_account(request):
    return render(request,'account.html')