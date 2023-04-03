from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Posts
from django.db.models import Q,CharField
from django.db.models.functions import Lower
CharField.register_lookup(Lower, "lower")


# Create your views here.

def categories(request):
    categories = Category.objects.all()
    posts = Posts.objects.all()
    print(posts)
    print(categories)
    Data = {'cat':categories, 'post':posts}
    return render(request, 'cat.html',Data)


def posts(request,pk):
    categories = Category.objects.all()
    arg = Posts.objects.filter(category_id_id=pk)
    arg1 = Category.objects.filter(id=pk)
    data = {'cat':categories,'arg': arg,'arg1':arg1}

    return render(request, 'post.html',data)


def search(request):
    categories = Category.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        searched = searched.lower()
        searched_post = Posts.objects.filter(Q(name__lower__contains=searched))
        data = {'cat':categories,'search': searched, 'searched': searched_post}
        return render(request, 'searched.html', data)
