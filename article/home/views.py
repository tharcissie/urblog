from carticle.forms import *
from django.db.models import Q
from django.forms import ModelForm
from django.urls import reverse_lazy
from carticle.models import Article, Comment
from django.views.generic import ListView, DetailView, RedirectView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from taggit.models import Tag

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags']=Tag.objects.all()
        return context
    


# class ArticleList(TagMixin,ListView):
#     model = Article
#     template_name = "home/home.html"


    
class TagListView(TagMixin,ListView):
    model = Article
    template_name = "home/tag.html"
    def get_queryset(self):
        return Article.objects.filter(tags__slug=self.kwargs.get('slug'))

    


class ArticleView(DetailView):
    model = Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['subject', 'message']

#################     function of rendering the homepage     ###################

def home(request):
    article = Article.objects.all()
    return render(request, 'home/home.html',{'article':article})


#################     function of article details and comment stuff     ###################

def article_details(request, pk, template_name='home/article_details.html'):
    article = get_object_or_404(Article, pk=pk)
    # article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article , reply=None).order_by('id')

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
    context = { 'object':article, 'comments':comments, 'comment_form':comment_form }  
    return render(request, template_name, context)

#####################     dealing with search features       ######################

class SearchResult(ListView):
    model = Article
    template_name = 'home/search.html'

    def get_queryset(self):
        search = self.request.GET.get('query')
       
        object_list = Article.objects.filter(

            Q(subject__icontains=search) | Q(message__icontains=search)
        )
        return object_list

class ArticleLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        print(pk)
        obj = get_object_or_404(Article, pk=pk)
        url_= obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_



class ArticleDislikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        print(pk)
        ob = get_object_or_404(Article, pk=pk)
        urll_= ob.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in ob.dislikes.all():
                ob.dislikes.remove(user)
            else:
                ob.dislikes.add(user)
        return urll_


