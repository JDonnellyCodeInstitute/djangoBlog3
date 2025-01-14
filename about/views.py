from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    # if request.method == "POST":
    #     print("Received a post request")
    collaborate_form = CollaborateForm() # data=request.POST

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )