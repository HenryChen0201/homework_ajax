from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'home/register.html', {'title':'取得圖片(圖)'})
def loadjason(request):
    return render(request, "home/loadjson.html", {'title': 'Homework'})