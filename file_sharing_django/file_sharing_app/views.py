from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'file_sharing_app/index.html', {})
