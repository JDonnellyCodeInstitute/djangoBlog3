from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

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

    # Post request for the comment
    if request.method == "POST":
        print("Received a post request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    # This resets the comment box to blank after a comment is added in the block above
    comment_form = CommentForm()

    print("About to render template")

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )