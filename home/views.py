from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreateForm
from django.contrib import messages


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home/post_list.html'
    
    def home(self, request):
        posts = Post.objects.all()
        return render(request, self.template_name, {"posts": posts})


class PostCreateView(LoginRequiredMixin, CreateView):
    Model = Post
    template_name ='home/post_form.html'
    form = CreateForm()

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    # def post(self, request, pk=None):
    #     form = CreateForm(request.POST, request.FILES or None)

    #     if not form.is_valid():
    #         ctx = {'form': form}
    #         return render(request, self.template_name, ctx)

    def post(self, request):
        
        if request.method == 'POST':
            form = CreateForm(request.POST)
            if form.is_valid():
                form.save()
                # return redirect("home")
        return render(request, self.template_name, {"form": form})


class PostDetailView(LoginRequiredMixin,  DetailView):
    Model = Post
    def post_detail(request, pk):
        post = Post.objects.get(id=pk)
        form = CreateForm(instance=post)
        if request.method == 'POST':
            form = CreateForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect("home")
        return render(request, "post_update.html", {"post": post, "form": form})

