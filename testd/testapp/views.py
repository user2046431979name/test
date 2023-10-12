from django.shortcuts import render
from django.views.generic import ListView, DetailView
 
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy

class index(ListView):
    model = Post
    template_name = 'index.html'
 
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): # новое изменение
    model = Post
    template_name = 'post_new.html'
    fields = ['title' , 'author' , 'body']




class BlogUpdateView(UpdateView): 
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
class BlogDeleteView(DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')

