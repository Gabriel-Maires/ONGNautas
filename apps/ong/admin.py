from django.contrib import admin
from .models import Post, Comments, Project, NewsletterUser


# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Project)
admin.site.register(NewsletterUser)