from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.




class PostList(ListView):
    model = Post




class PostDetail(DetailView):
    model = Post



class PostCreate():
    pass



class PostDelete():
    pass




# def post_list(request):
#     post_list = Post.objects.all()
#     return render(request, 'post/list.html', {'post_list' : post_list})





# def post_details(request, id):
#     pass