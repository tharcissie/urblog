from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
# from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import Article, Comment, College
from django.urls import reverse_lazy
from django.forms import ModelForm
from .forms import *



class ArticleList(ListView):
    model = Article
    template_name = 'carticle/article_list.html'

    

class ArticleView(DetailView):
    model = Article

class ArticleCreate(CreateView):
    model = Article
    fields = ['subject', 'message', 'picture' ]
    success_url = reverse_lazy('article_list')

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['subject', 'message', 'picture']
    success_url = reverse_lazy('article_list')

class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['subject', 'message','college', 'picture']
def article_list(request, template_name='carticle/article_list.html'):
    article = Article.objects.all()
    data = {}
    data['object_list'] = article
    return render(request, template_name, data)



def article_detail(request, pk, template_name='carticle/article_detail.html'):
    article = get_object_or_404(Article, pk=pk)

    is_liked=False
    if article.likes.filter(pk=request.user.id).exists():
        article.likes.remove(request.user)
        is_liked=True


    comments = Comment.objects.filter(article=article, reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
             content = request.POST.get('content')
             reply_id = request.POST.get('comment_id')
             comment_qs = None
             if reply_id:
                 comment_qs = Comment.objects.get(id=reply_id)
             comment = Comment.objects.create(article=article, user=request.user, content=content, reply=comment_qs)
             comment.save() 
             return redirect('article_list')
    comment_form = CommentForm()

    

    context = { 'object':article, 'comments':comments, 'comment_form':comment_form, 'is_liked':is_liked, 'total_likes':article.total_likes(),}  
    return render(request, template_name, context)



def article_like(request):
    article = get_object_or_404(Article, pk='article_id')
    is_liked=False
    if article.likes.filter(pk=request.user.id).exists():
        article.likes.remove(request.user)
        is_liked=False
    else:
        article.likes.add(request.user)
        is_liked=True
    return HttpResponseRedirect(article.get_absolute_url())
        



@login_required
def article_create(request, template_name='carticle/article_form.html'):
    form = ArticleForm(request.POST,files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, template_name, {'form':form})

@login_required
def article_update(request, pk, template_name='carticle/article_form.html'):
    article= get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST,files=request.FILES, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, template_name, {'form':form})

@login_required
def article_delete(request, pk, template_name='carticle/article_confirm_delete.html'):
    article= get_object_or_404(Article, pk=pk)    
    if request.method=='POST':
        article.delete()
        return redirect('article_list')
    return render(request, template_name, {'object':article})


class ArticleCollege(ListView):
    model = Article
    template_name = 'carticle/colleges.html'

    def get_queryset(self):
        self.college = get_object_or_404(College, pk=self.kwargs['pk'])
        
        return Article.objects.filter(college=self.college)

    def get_context_data(self, **kwargs):
        context = super(ArticleCollege, self).get_context_data(**kwargs)
        context['college'] = self.college
        return context
    
  
