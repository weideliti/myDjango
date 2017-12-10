# _*_ coding: utf-8 _*_
__author__ = 'weide'
__date__ = '2017/11/7 19:11'
import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc','detail','degree', 'learn_time', 'students','click_nums','fav_nums','add_time']
    search_fields =['name', 'desc','degree', 'learn_times', 'fav_nums','add_time']
    list_filter = ['name', 'desc', 'degree', 'fav_nums','add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields =['course', 'name', 'add_time']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
        list_display = ['course', 'name', 'add_time']
        search_fields = ['course', 'name', 'add_time']
        list_filter = ['course__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'add_time']
    list_filter = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)