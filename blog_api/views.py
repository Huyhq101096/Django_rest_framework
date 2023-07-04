from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import DjangoModelPermissions, BasePermission



class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user



class PostList(generics.ListCreateAPIView):
    # tra ve all post co du lieu la status = 'published'
    # permission_classes = [IsAdminUser]
    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all() 
    serializer_class = PostSerializer
 

class PostDetail(generics.RetrieveDestroyAPIView, PostUserWritePermission):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

