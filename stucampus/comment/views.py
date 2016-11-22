from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from stucampus.comment.models import Comment
from stucampus.comment.forms import CommentForm
from stucampus.utils import get_client_ip, spec_json
from stucampus.articles.models import Article
import json

def del_comment(request):
    try:
        comment_id = request.POST['id']
        comment = get_object_or_404(Comment, pk=comment_id)
        article_id = comment.article.id
        if request.user.is_authenticated():
            comment.delete()
            comment.article.comments -=1
            comment.article.save()
            return HttpResponse(comment_id)
        else:
            return spec_json(status='errors')
    except Exception as e:
        raise e

def comment_upload(request):
    article_id = request.POST['article_id']
    comm_content = request.POST['content']
    if(comm_content==""):
        return spec_json(status='errors')
    else:
        try:
            if request.user.is_authenticated():
                comment = Comment.objects.create(
                    content = comm_content,
                    editor = request.user.student,
                    create_ip = get_client_ip(request),
                    article = Article.objects.get(id=article_id)
                )
                comment.article.comments +=1
                comment.article.save()
                comment.save()
                info = {
                    'content':comm_content,
                    'screen_name':comment.editor.screen_name,
                    'create_date':comment.create_date.isoformat(),
                    'comment_id':comment.id,
                }
                my_json = json.dumps(info)
                return  HttpResponse(my_json, content_type="application/json")
            else:
                return spec_json(status='errors')
        except Exception as e:
            raise e
