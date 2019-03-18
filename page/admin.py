from django.contrib import admin
from .models import Comment, Contact, Projects, RelatedImages, Reference

admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Projects)
admin.site.register(RelatedImages)
admin.site.register(Reference)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'comment_name', 'text']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'name', 'phone', 'mail', 'message']

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_main_image', 'project_description', 'project_description_details']

class RelatedImages(admin.ModelAdmin):
    list_display = ['projects', 'project_image']

class Reference(admin.ModelAdmin):
    list_display = ['opinion']




