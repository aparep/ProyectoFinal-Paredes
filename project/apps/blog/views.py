from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def about(request):
    return render(request, 'blog/about.html')

def post_listar(request):
    posts= models.Post.objects.all()
    context = {'posts':posts}
    return render(request, "blog/post_listar.html", context)

def post_crear(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_listar')
    else:
        form = forms.PostForm()
    return render(request, 'blog/post_crear.html', {'form': form})