from django.shortcuts import render
from .forms import MyForm

def converter_view(request):
    form = MyForm()
    return render(request,'index.html',{'form':form})