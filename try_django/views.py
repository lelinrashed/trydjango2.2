from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from blog.models import BlogPost
from try_django.forms import ContactForm


def home_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {
        "blog_list": qs,
        "title" : "Welcome to try django 2.2"
    }
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title" : "About us"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact us",
        "form": form
    }
    template_name = "form.html"
    return render(request, template_name, context)


def example_page(request):
    context = {"title" : "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return  HttpResponse(rendered_item)

