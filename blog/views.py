from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    # This retrieves all the published posts
    queryset = Post.objects.filter(status=1) 
    # This stops incorrect inputs - if the slug is input incorrectly, or theres a 404 this activates 
    post = get_object_or_404(queryset, slug=slug)
    # All comments ordered in terms of recency
    comments = post.comments.all().order_by("-created_on")
    # Number of approved comments
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
        },
    )