from django.shortcuts import render

from .forms import MessageForm

# Create your views here.
def home(request):
    
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'index.html', context)

def music(request):
    return render(request, 'music.html')

def vlog(request):
    return render(request, 'vlog.html')

def photo(request):
    return render(request, 'photo.html')

def love(request):
    return render(request, 'love.html')