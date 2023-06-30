from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    # tra ve all post co du lieu la status = 'published'
    queryset = Post.postobjects.all() 
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass
