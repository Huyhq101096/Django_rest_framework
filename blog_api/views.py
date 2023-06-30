from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    # tra ve all post co du lieu la status = 'published'
    queryset = Post.postobjects.all() 
    serializer_class = PostSerializer
 

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

