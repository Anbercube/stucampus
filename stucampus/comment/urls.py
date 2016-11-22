from django.conf.urls import url, patterns
from stucampus.comment.views import del_comment,comment_upload

urlpatterns = [
    url(r'^del_comment/', del_comment, name='del_comment'),
    url(r'^comment_upload/', comment_upload, name='comment_upload'),
]
