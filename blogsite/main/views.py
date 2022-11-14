from django.shortcuts import render
from .forms import AddBlog

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def blog(request):
    form_result = ''
    if request.method == 'POST':
        form = AddBlog(request.POST)
        if form.is_valid():
            try:
                form.save()
                form_result = 'Saqlandi'
            except:
                form_result = 'Xatolik boldi'

    else:
        form = AddBlog()

    return render(request, 'main/blog.html', {'form': form, 'f_r': form_result})


def login_page(request):
    return render(request, 'main/login.html')


def register_page(request):
    return render(request, 'main/register.html')
