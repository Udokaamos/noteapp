from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import CreateForm
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home/post_list.html"

    def get(self, request):
        post_list = Post.objects.all()
        ctx = {'post_list': post_list}
        return render(request, self.template_name, ctx)

#     def get_queryset(self):
# #         # if there is a search query in the URL parameter, then use it to filter the results
#         search_query = self.request.GET.get('search', '')
# #         # using Q for case-insensitive search in a MySQL database
# #         # filtering for posts where the user is the author
#         queryset = Post.objects.filter(Q(content__lower__contains=search_query)).filter(author_id=self.request.user.id).order_by('-date_posted')
#         return queryset   

    # def post(self, request):
    #     form = CreateForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         post.save()

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'home/post_form.html'
    # success_url = reverse_lazy('home:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        post = form.save(commit=False)
        post.owner = self.request.user
        post.save()
        return reverse('post_detail', args=[post.id])

class PostDetailView(LoginRequiredMixin, View):
    model = Post
    template_name = "home/post_detail.html"

    def get(self, request, pk) :
        post = self.objects.get(id=pk)
        context = { 'post':post}
        return render(request, self.template_name, context)


# def post(request):
#     postid = int(request.GET.get('postid', 0))
#     posts = Post.objects.all()

#     if request.method == 'POST':
#         postid = int(request.POST.get('postid', 0))
#         title = request.POST.get('title')
#         text = request.POST.get('text', '')

#         if postid > 0:
#             post = Post.objects.get(pk=postid)
#             post.title = title
#             post.text = text
#             post.save()

#             return redirect('/?postid=%i' % postid)
#         else:
#             document = Post.objects.create(title=title, text=text)

#             return redirect('/?postid=%i' % post.id)

#     if postid > 0:
#         post = Post.objects.get(pk=postid)
#     else:
#         post = ''

#     context = {
#         'postid': postid,
#         'posts': posts,
#         'post': post
#     }

#     return render(request, 'base.html', context)

# def delete_post(request, postid):
#     post = Post.objects.get(pk=postid)
#     post.delete()

#     return redirect('/?postid=0')



    #  def post(self, request, pk=None):
    #     form = CreateForm(request.POST, request.FILES or None)

    #     if not form.is_valid():
    #         ctx = {'form': form}
    #         return render(request, self.template_name, ctx)


    # def get(self, request):
    #     form = CreateForm()
    #     posts = Post.objects.all().order_by('date_posted')
    #     users = User.objects.exclude(id=request.user.id)
    

        # ctx = {
        #     'form': form, 'post': posts, 'users': users
        # }
        # return render(request, self.template_name, ctx)



# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = CreateForm() # making the class use an existing form with pre-defined validation rules
#     template_name = 'home/post_form.html'
#     success_url = '/'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#             text = form.cleaned_data['post']
#             form = CreateForm()
#             return redirect('home:home')

#         args = {'form': form, 'text': text}
#         return render(request, self.template_name, args)