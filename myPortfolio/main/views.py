from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Info, AboutMe, Contact, MyUsers, Blog
from .forms import AddContact, CreateUsersForm
import telegram_send
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from myPortfolio.settings import LOGIN_URL

# LOGIN_URL = 'login'

# Create your views here.
@login_required(login_url='login')
def index(request):
    infos = Info.objects.filter()
    contex = {
        'title': 'Sayt',
        'infos': infos

    }
    return render(request, 'main/index.html', contex)


# @login_required(login_url='login')
class About(TemplateView):
    about_infos = AboutMe.objects.all().filter(type='about', state=1)
    gap_info = AboutMe.objects.filter(type='gap')
    template_name = 'main/about.html'
    contex = {
        'title': 'Biz haqimizda',
        'infos': about_infos,
        'gapinfo': gap_info[0]

    }
    extra_context = contex




# @login_required(login_url='login')
class MyWorks(TemplateView):
    template_name = 'main/myworks.html'


@login_required(login_url='login')
def contact(request):
    form_result = ''
    if request.method == 'POST':
        form = AddContact(request.POST)
        if form.is_valid():
            try:
                name = request.POST['name']
                email = request.POST['email']
                subject = request.POST['subject']
                xabar = request.POST['message']

                form.save()
                form_result = 'Raxmat ......'
                telegram_send.send(messages=[f'Xabar keldi: \n Ismi: {name} \n Email: {email} \n '
                                             f'Mavzu: {subject} \n Xabar: {xabar}'])

            # try:
            #        Contact.objects.create(**form.cleaned_data)
            #
            #        return redirect('contact')
            except:
                form_result = 'Xatolik boldi'
            #        form.add_error(None, 'Xatolik sodir boldi')
            # print(form.cleaned_data)

    else:  # aks holda yani foydalanuvchi hechqanday button bosmasdan sahifaga turibti yoki kirgan
        form = AddContact()

    return render(request, 'main/contact.html', {'form': form, 'f_r': form_result})


def login_page(request):
    error = ''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = 'Parol yoki username xato!!!'

    context = {'error': error}
    return render(request, 'main/login.html', context)


def register(request):
    error = ''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUsersForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                usr = MyUsers(username=username, password=password)
                usr.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')

                return redirect('home')

            else:
                error = 'Qanaqadir xatolik bo\'ldi'
    context = {'error': error}
    return render(request, 'main/register.html', context)



def logout_users(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def blog(request):
    bloglar = Blog.objects.all().order_by('-created_at')
    message = ''


    if request.method == 'POST':
        try:
            username = request.user.username
            title = request.POST.get('title')
            blog = request.POST.get('blog')
            obj = Blog(username=username, title=title, blog=blog)
            obj.save()
            message = 'Saqlandi'
        except:
            message = 'Xatolik yuz berdi!'
    context = {'message': message, 'bloglar': bloglar}


    return render(request, 'main/blog.html', context)



@login_required(login_url='login')
def search(request):
    malumot = request.GET.get('s')
    bloglar = Blog.objects.filter(Q(title__icontains=malumot) | Q(blog__icontains=malumot) | Q(username__icontains=malumot))
    return render(request, 'main/search.html', {'bloglar': bloglar})


# class Search(ListView, LoginRequiredMixin):
#     login_url = 'login'
#     redirect_field_name = LOGIN_URL
#     model = Blog
#     template_name = 'search'
#     def get_queryset(self):
#         malumot = self.request.GET.get('s')
#         bloglar = Blog.objects.filter(
#             Q(title__icontains=malumot) | Q(blog__icontains=malumot) | Q(username__icontains=malumot))
#         return bloglar

@login_required(login_url='login')
def profile(request):
    current_user = request.user
    user = MyUsers.objects.filter(username=current_user.username)

    if len(user) != 0:
        if user[0].image:
            rasm = user[0].image.url
        else:
            rasm = ''
        username = user[0].username
        full_name = user[0].full_name
        phone_number = user[0].phone_number
        facebook = user[0].facebook
        twitter = user[0].twitter
        instagram = user[0].instagram
        context = {
            'rasm': rasm,
            'username': username,
            'full_name': full_name,
            'phone_number': phone_number,
            'facebook': facebook,
            'twitter': twitter,
            'instagram': instagram

        }
        return render(request, 'main/profile.html', context)

    else:
        error = 'Iltimos logout qilib qayta login qiling'
        return render(request, 'main/profile.html', {'error': error})


@login_required(login_url='login')
def edit(request):
    current_user = request.user
    user = MyUsers.objects.filter(username=current_user.username)
    full_name = user[0].full_name
    phone_number = user[0].phone_number
    facebook = user[0].facebook
    twitter = user[0].twitter
    instagram = user[0].instagram
    context = {
            'full_name': full_name,
            'phone_number': phone_number,
            'facebook': facebook,
            'twitter': twitter,
            'instagram': instagram
    }
    if request.method == 'POST':
        full_name1 = request.POST.get('full_name')
        phone_number1 = request.POST.get('phone_number')
        instagram1 = request.POST.get('instagram')
        twitter1 = request.POST.get('twitter')
        facebook1 = request.POST.get('facebook')
        this_user = MyUsers.objects.get(username=current_user.username)
        this_user.full_name = full_name1
        this_user.phone_number = phone_number1
        this_user.instagram = instagram1
        this_user.twitter = twitter1
        this_user.facebook = facebook1
        if request.POST.get('image'):
            this_user.image = request.POST.get('image')
        else:
            this_user.image = '/blank-profile-picture-973460_1280.jpg'
        this_user.save()
        return redirect('profile')


    return render(request, 'main/edit.html', context)
