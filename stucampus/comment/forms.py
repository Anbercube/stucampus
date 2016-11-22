# coding: utf-8#
from django import forms
from stucampus.comment.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = { 
            'content' : forms.Textarea(attrs={
                'class' : 'addcomment',
                'placeholder' : "说点什么吧...",
            }),                    
        }
        error_messages = {
            'content': {
                'blank' : ("评论不能为空"),
            },
        }

