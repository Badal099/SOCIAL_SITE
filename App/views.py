from django.db.models import query
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from App.models import *
from django.db.models import Q

# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    posts = Post.objects.all()
    d = {'posts': posts}
    return render(request, 'home.html', d)


def upload(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    if request.method == "POST":
        des = request.POST['des']
        image = request.FILES['image']
        u = User.objects.filter(fullname=request.user.fullname).first()
        Post.objects.create(
            user=u, des=des, image=image)
        return redirect('profile')

    return render(request, 'upload.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(user=user)
    d = {'posts': posts, 'user': user}
    return render(request, 'profile.html', d)


def search(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')

    if request.method == 'POST':
        query_original = request.POST.get('q')
        if query_original != None:
            lookups = User.objects.filter(Q(fullname__icontains=query_original) | Q(
                contact__icontains=query_original) | Q(email__icontains=query_original))
            return render(request, 'search.html', {'lookups': lookups})

    return render(request, 'search.html')


def autosuggest(request):
    query_original = request.GET.get('term')
    queryset = User.objects.filter(Q(fullname__icontains=query_original) | Q(
        contact__icontains=query_original) | Q(email__icontains=query_original))
    list = []
    list += [x.fullname for x in queryset]
    return JsonResponse(list, safe=False)
