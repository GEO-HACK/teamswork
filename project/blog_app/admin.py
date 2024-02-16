from django.contrib import admin
from .models import Blog
from .models import Contact
from .models import Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Comment)
