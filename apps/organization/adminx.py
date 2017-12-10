# _*_ coding: utf-8 _*_
__author__ = 'weide'
__date__ = '2017/11/7 19:11'

import xadmin
from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums','image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums','image', 'address', 'city', 'add_time']
    list_filter = ['name', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']



class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'fav_nums', 'work_years']
    list_filter =  ['org', 'name', 'fav_nums', 'work_years']


xadmin.site.register( CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)