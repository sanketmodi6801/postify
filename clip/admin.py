from django.contrib import admin

# Register your models here.
from .models import Posts, Category

admin.site.register(Category)
admin.site.register(Posts)
