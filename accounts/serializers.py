from rest_framework import serializers
from .models import User
from .models import Comment
#---------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
#---------------------------
class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phoneNumber','full_name','is_admin','is_active','email')
#---------------------------
class CommentSerializer(serializers.ModelSerializer):
    user_full_name = serializers.ReadOnlyField(source='user.full_name')
    class Meta:
        model = Comment
        fields = ('id', 'user', 'user_full_name', 'text', 'created', 'valid', 'rating', 'likes', 'dislikes', 'parent_comment')
#---------------------------