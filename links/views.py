from django.shortcuts import render, get_object_or_404, redirect
from .models import Link
from django.urls import reverse

from .forms import LinkForm


# Create your views here.
def shortlink(request):
    links = Link.objects.all()  # allows us to get all the links from view in the index.html page
    context = {
        "links": links
    }
    return render(request, 'links/index.html', context)


# oursite.com/google -->> google.com

def root_link(request, link_slug):  # pass in the link_slug so we know which link we workin w/
    link = get_object_or_404(Link, slug=link_slug)  # either get this link or pass error 404
    link.click()  # this will increment the click field
    return redirect(link.url)


# return something to the user --> return a redirect(import redirect)


def add_link(request):
    if request.method == "POST":    # add some logic (see if the request if a get or post method)
        form = LinkForm(request.POST)
        if form.is_valid():
            # if the form is valid - then process
            # save the data and return user to homepage
            form.save()
            return redirect(reverse('home')) #import reverse --. redirect user to homepage after form is saved

    else: #if its a GET then enter a blank form & create
        form = LinkForm()

    context = {
        "form": form
    }
    return render(request, 'links/create.html', context)
