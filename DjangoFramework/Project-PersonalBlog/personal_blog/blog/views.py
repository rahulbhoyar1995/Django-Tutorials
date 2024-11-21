from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .models import Comment


def post_list(request):
    category_slug = request.GET.get('category')
    posts = Post.objects.filter(category__slug=category_slug) if category_slug else Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        author = request.POST['author']
        content = request.POST['content']
        Comment.objects.create(post=post, author=author, content=content)
    return render(request, 'blog/post_detail.html', {'post': post})
