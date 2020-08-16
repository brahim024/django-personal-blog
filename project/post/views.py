from django.shortcuts import render
from .models import Post
# Create your views here.

def post(request):
    post= Post.objects.all()
    return render(request,'all_post.html',{'pos':post})
def post_details(request,id):
    post_details= Post.objects.get(id=id)
    return render(request,'post_details.html',{'onepost':post_details})
