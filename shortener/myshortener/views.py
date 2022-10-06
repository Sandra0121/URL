from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return render(request, 'myshortener/index.html')

def create_view(request):
    if request.method == 'POST':
        link =request.POST['link']
        uid =str(uuid.uuid4())[:5]
        new_url =Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
    
def go_view(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)