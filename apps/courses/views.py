# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from .models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class CourseListView(View):
   def get(self,request):
       all_course = Course.objects.all().order_by("-add_time")

       hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        #课程排序
       sort = request.GET.get('sort',"")
       if sort:
           if sort == "student":
               all_course =all_course.order_by("-students")
           elif sort == "hot":
               all_course=all_course.order_by("-click_nums")


        #对课程进行分页
       try:
           page = request.GET.get('page', 1)
       except PageNotAnInteger:
           page = 1

           # objects = ['john', 'edward', 'josh', 'frank']

           # Provide Paginator with the request object for complete querystring generation

       p = Paginator(all_course, 6, request=request)  # 5每一页显示5个

       courses = p.page(page)


       return render(request,'course-list.html', {
           'all_course':courses,
           'sort':sort,
           'hot_courses':hot_courses
       })


