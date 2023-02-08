from django.shortcuts import render
from checkapp.models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def index(request):
    return render(request,'checkapp/index.html')

from django.shortcuts import render,get_object_or_404
from checkapp.models import Post

from taggit.models import Tag
def postlistview(request,tag_slug=None):
    post=Post.objects.all().order_by('companey')
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post=post.filter(tags__in=[tag])
    paginator=Paginator(post,5)
    page_number=request.GET.get('page')
    try:
        post=paginator.page(page_number)
    except PageNotAnInteger:
        post=paginator.page(1)
    except EmptyPage:
        post=paginator.page(paginator.num_pages)
    return render(request,'checkapp/postlist.html',{'p':post,'tag':tag})

def postlistviewb(request,tag_slug=None):
    post=Post.objects.all().order_by('-companey')
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post=post.filter(tags__in=[tag])
    paginator=Paginator(post,5)
    page_number=request.GET.get('page')
    try:
        post=paginator.page(page_number)
    except PageNotAnInteger:
        post=paginator.page(1)
    except EmptyPage:
        post=paginator.page(paginator.num_pages)
    return render(request,'checkapp/postlist.html',{'p':post,'tag':tag})

def postlistviewc(request,tag_slug=None):
    post=Post.objects.all().order_by('publish')
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post=post.filter(tags__in=[tag])
    paginator=Paginator(post,5)
    page_number=request.GET.get('page')
    try:
        post=paginator.page(page_number)
    except PageNotAnInteger:
        post=paginator.page(1)
    except EmptyPage:
        post=paginator.page(paginator.num_pages)
    return render(request,'checkapp/postlist.html',{'p':post,'tag':tag})

def postlistviewp(request,tag_slug=None):
    post=Post.objects.all().order_by('-publish')
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post=post.filter(tags__in=[tag])
    paginator=Paginator(post,5)
    page_number=request.GET.get('page')
    try:
        post=paginator.page(page_number)
    except PageNotAnInteger:
        post=paginator.page(1)
    except EmptyPage:
        post=paginator.page(paginator.num_pages)
    return render(request,'checkapp/postlist.html',{'p':post,'tag':tag})


from django.core.mail import send_mail
from checkapp.forms import EmailSendForm

def mailsendview(request,id):
     post=get_object_or_404(Post,id=id,status='published')
     sent=False
     if request.method=='POST':
         form=EmailSendForm(request.POST)
         if form.is_valid():
             cd=form.cleaned_data
             p_url=request.build_absolute_uri(post.get_absolute_url())
             subject='{}({}) recommends you to read "{}"'.format(cd['name'],cd['email'],post.companey)
             message='Read Post At:\n {}\n\n\'Comments:\n{}'.format(p_url,cd['name'],cd['comments'])
             send_mail(subject,message,'gln@blog.com',[cd['to']])
             sent=True
     else:
         form=EmailSendForm()
         return render(request,'checkapp/sharebyemail.html',{'po':post,'fo':form,'sent':sent})

from checkapp.models import Comment
from checkapp.forms import CommentForm
def postdetail_view(request,year,month,day,post):
 postd=get_object_or_404(Post,slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
 #comments=post.comeents.filter(active=True)
 csubmit=False
 if request.method=='POST':
     form=CommentForm(request.POST)
     if form.is_valid():
         new_comment=form.save(commit=False)
         new_comment.post=postd
         new_comment.save()
         csubmit=True
 else:
    form=CommentForm()
 return render(request,'checkapp/postdetail.html',{'pd':postd,'fd':form,'csubmit':csubmit})
