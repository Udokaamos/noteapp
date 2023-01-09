from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import CreateForm

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home/post_list.html"

    def get(self, request):
        form = CreateForm()
        posts = Post.objects.all().order_by('date_posted')
        users = User.objects.exclude(id=request.user.id)
    

        args = {
            'form': form, 'post': posts, 'users': users
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = CreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = CreateForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)