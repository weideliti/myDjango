# _*_ coding: utf-8 _*_
__author__ = 'weide'
__date__ = '2017/11/7 19:11'
import xadmin
from .models import UserAsk, UserCourse, UserMessage, UserFavorite, CourseComment

class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name','add_time']
    search_fields = ['name', 'mobile', 'course_name','add_time']
    list_filter =['name', 'mobile', 'course_name','add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields =['user', 'course', 'add_time']
    list_filter = ['user', 'course', 'add_time']



class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserFavoriteAdmin(object):
        list_display = ['user', 'fav_id', 'fav_type', 'add_time']
        search_fields = ['user', 'fav_id', 'fav_type', 'add_time']
        list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class CourseCommentAdmin(object):
            list_display = ['user', 'course', 'comments', 'add_time']
            search_fields =['user', 'course', 'comments', 'add_time']
            list_filter = ['user', 'course', 'comments', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)