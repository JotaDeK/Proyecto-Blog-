from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Like


def user_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render (request, "blog.html", {"posts": posts, "total_posts": total_posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    total_likes = post.likes.count()
    context = {
        "post": post,
        "total_likes": total_likes,
    }
    return render(request, "post_detail.html", context)


@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[str(post.id)]))
    else:
        return HttpResponseRedirect(reverse('post_detail', args=[str(post.id)]))





