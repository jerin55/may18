from django import template
from requests import request

from network.models import *





register = template.Library()



@register.filter
def delprice(value):

    value1 = value *25/100

    value2 = value+value1

    
    return value2


@register.filter
def counts(value):

    posts = Post.objects.filter(intr_id=value)
    
    return len(posts)

@register.filter
def counts2(value,value2):

    posts = Post.objects.filter(intr_id=value,creater=value2)
    
    return len(posts)


@register.filter
def views_count(post_id):

    post = Post.objects.get(id=post_id)
    views = PostViewer.objects.filter(post=post).count()
    
    return views

@register.filter
def notification_read(value):

    notification = Notifications.objects.get(id=value)
    notification.is_read = True
    notification.save()
    
    return

@register.filter
def page_notifications(value1,value2):
    page_noti_count = 0
    page_notification =  Notifications.objects.filter(to_user=value2,is_read=0)
  
    for i in page_notification:
        if(i.pages != None):
            if i.pages.id == value1:
                if i.type == "User_Accept_Page_Invitions":
                    page_noti_count = page_noti_count+1
                
                if i.type == "User_Page_Join_Request":
                    page_noti_count = page_noti_count+1

                if i.type == "Page_Post_Reviwes":
                    page_noti_count = page_noti_count+1

    return page_noti_count