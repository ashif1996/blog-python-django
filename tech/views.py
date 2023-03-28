from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.http import HttpResponseRedirect


class Home(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']
    # ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__iexact=cats.replace('-', ' '))
    return render(request, 'categories.html',
                  {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        get_id = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = get_id.total_likes()
        liked = False
        if get_id.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')


class AddCategory(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title', 'body')


class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'body']


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')


class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    ordering = ['-date_added']
    # fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('article-details', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


