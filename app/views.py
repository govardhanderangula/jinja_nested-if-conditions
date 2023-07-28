from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={"a":20,"b":5,"c":10}
    return render(request,'data_render.html',context=d)
