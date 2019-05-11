from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost
from searches.models import SearchQuery


def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        context["blog_list"] = blog_list
    return render(request, 'searches/view.html', context)