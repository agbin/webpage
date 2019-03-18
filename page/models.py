from django.db import models
from django.utils import timezone
from django.urls import reverse


class Comment(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    comment_name = models.CharField(max_length=50, default='text')
    text = models.TextField(default='text')


class Contact(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=60, default='text')
    phone = models.IntegerField()
    mail = models.EmailField()
    message = models.TextField(default=1)





class Projects(models.Model):
    project_name = models.CharField(max_length=200, default='text')
    project_main_image = models.FileField(max_length=1000, upload_to='page/%Y/%m/%d', blank=True, null=True)
    project_description = models.TextField(max_length=5000, default='text')
    project_description_details = models.TextField(max_length=5000, default='text')

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.project_name


class RelatedImages(models.Model):
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True, blank=True)
    project_image = models.FileField(max_length=1000, upload_to='page/%Y/%m/%d', blank=True, null=True)


class Reference(models.Model):
    opinion = models.FileField(max_length=1000, upload_to='page/%Y/%m/%d', blank=True, null=True)