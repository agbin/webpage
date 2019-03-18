from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from .models import Comment, Contact, Projects, RelatedImages, Reference
from .forms import CommentForm, ContactForm, ProjectForm
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic


def base(request):
    return render_to_response('page/base4.html', {})


def base(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        contactform = ContactForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data['text'],
                name=form.cleaned_data['name'],
            )
            Contact.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                mail=form.cleaned_data['mail'],
                message=form.cleaned_data['message'],
            )
            return redirect("details")
    else:
        form = CommentForm()
        contactform = ContactForm()
    return render(request, 'page/details.html', {'form': form, 'contactform': contactform,})


def message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                mail=form.cleaned_data['mail'],
                message=form.cleaned_data['message'],
            )
            return render(request, 'page/message.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'page/message.html', {'form': form})


def about_us(request):
    return render_to_response('page/about.html', {})

def projects(request):
    images = Projects.objects.all()
    return render_to_response('page/projects.html', {'images': images})

class Project_Detail(View):
    def get(self, request, pk):
        project = get_object_or_404(Projects, pk=pk)
        related_images = RelatedImages.objects.filter(projects=pk)
        return render(request, 'page/project_gallery.html', {'project': project, 'related_images': related_images})


def offers(request):
    return render_to_response('page/offer.html', {})



def reference(request):
    references = Reference.objects.all()
    return render_to_response('page/references.html', {'references': references})

# def gallery(request):
#     return render_to_response('page/project_gallery.html', {})

# class CommentsList(View):
#     def get(self, request):
#         form = ContactForm()
#         comments = Comment.objects.all()
#         return render(request, 'page/base4.html', {"form": form, 'comments': comments})
#
#     def post(self, request):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             Comment.objects.create(
#                 text=form.cleaned_data['text'],
#                 name=form.cleaned_data['name'],
#             )
#             return redirect("comments")
#
#
#
# def message(request):
#
#     form_class = ContactForm
#
#     if request.method == 'POST':
#         form = form_class(data=request.POST)
#         # ... more code from above ...
#     else:
#         form = form_class() # this is important
#
#     return render(request, 'page/message.html', {
#         'form': form,  # NOTE: instead of form_class!!!!
#     })




# def project_add(request):
#     # if request.user.is_authenticated:
#         if request.method == "POST":
#             form = ProjectAddForm(request.POST, request.FILES)
#             if form.is_valid():
#                 post = form.save(commit=False)
#
#                 post.author = request.user
#                 post.published_date = timezone.now()
#                 post.save()
#                 return redirect('post_detail', pk=post.pk)
#         else:
#             form = PostForm()
#             return render(request, 'items/post_edit.html', {'form': form})
#     # else:
#     #     return render(request, 'items/notlogged.html')





class ProjectCreate(CreateView):
    model = Projects
    fields = '__all__'
    success_url = reverse_lazy('projects')


class ProjectUpdate(UpdateView):
    model = Projects
    fields = '__all__'
    success_url = reverse_lazy('projects')


# class ProjectDelete(DeleteView):
#     model = Projects
#     success_url = reverse_lazy('')










def search(request):
    form = SearchForm()
    return render(request, 'page/base4.html', {'form': form})





class Login(View):
    def get(self, request):
        return render(request, "page/login.html", {'user': request.user})
    def post(self, request):
        login1 = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(username=login1, password=password)
        if user:
            login(request, user)
            return redirect('post_list')
        return HttpResponse("ERROR %s %s" % (login1, password))


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("post_list")