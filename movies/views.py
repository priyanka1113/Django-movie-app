from django.shortcuts import render,HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("My Favourite Movies")



def index(request):
    context={
        'movies':['Rockie','Friends with Benefits','Mission Impossible','La La Land','Red Alert']

    }
    return render(request,'movies/index.html',context)

def about(request):
    return render(request,'movies/about.html',{})