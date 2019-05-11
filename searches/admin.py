from django.contrib import admin

# Register your models here.
from searches.models import SearchQuery

admin.site.register(SearchQuery)
