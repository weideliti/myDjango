# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import CourseOrg, CityDict
from .forms import UserAskForm
from operation.models import UserFavorite,UserMessage


class OrgView(View):

    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        all_citys = CityDict.objects.all()
        org_nums = all_orgs.count()


        #取出筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
            org_nums = all_orgs.count()



        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 3,request=request)  #5每一页显示5个

        orgs = p.page(page)


        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            "city_id":city_id,
        })


class AddUserView(View):
    #用户添加咨询
    def post(self,request):
        userask_form = UserAskForm(request.Post)
        if userask_form.valid():
            user_ask=userask_form.save(commit=True) #提交保存导数据库
            #用modelform，不需要一个一个把值存入，能自动将定义好的属性存入
            return HttpResponse("{'status'': 'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status': 'fail','msg':'添加错误'}",content_type='application/json')
            #return HttpResponse("{'status': 'fail','msg':{0}}".format(userask_form.errors),
            #                   content_type='application/json')

class OrgHomeView(View):
    """
    机构首页
    """
    def get(self, request, org_id):
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav =False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id,fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.all()[:3] #通过外键Coures进入Course表取出对应机构的所有课程
        all_teachers = course_org.teacher_set.all()[:1] #通过外键Coures进入teacher表取出对应机构的所有教师
        return render(request,'org-detail-homepage.html', {
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            'course_org':course_org,
            'has_fav': has_fav,
            'current_page':current_page
        })


class OrgCourseView(View):
    """
    机构课程
    """
    def get(self, request, org_id):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav =False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id,fav_type=2):
                has_fav = True
        all_courses = course_org.course_set.all() #通过外键Coures进入Course表取出对应机构的所有课程
        return render(request,'org-detail-course.html', {
            'all_courses':all_courses,
            'course_org':course_org,
            'has_fav': has_fav,
            'current_page': current_page,
        })


class OrgDescView(View):
    """
    机构介绍
    """
    def get(self, request, org_id):
        current_page = "desc"
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav =False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id,fav_type=2):
                has_fav = True
        return render(request,'org-detail-desc.html', {
            'course_org':course_org,
            'has_fav': has_fav,
            'current_page':current_page
        })


class OrgTeachersView(View):
    """
    机构讲师
    """
    def get(self, request, org_id):
        current_page ="teachers"
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav =False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id,fav_type=2):
                has_fav = True
        all_teachers = course_org.teacher_set.all()#通过外键进入teacher表取出对应机构的所有课程
        return render(request,'org-detail-teachers.html', {
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page': current_page,
            'has_fav':has_fav,
        })


class AddFavView(View):
    """
    用户收藏功能
    """
    def post(self,request):
        fav_id =request.POST.get('fav_id',0)
        fav_type = request.POST.get('fav_type',0)

        if not request.user.is_authenticated():
            #判断是否是登录状态
            return HttpResponse({"status":"fail","msg":"用户未登录"}, content_type='application/json')

        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id),fav_type=int(fav_type))
        if exist_records:
            exist_records.delete()
            return HttpResponse({"status": "success", "msg": "收藏"}, content_type='application/json')
        else:
            user_fav=UserFavorite()
            if int(fav_id)>0 and int(fav_type)>0:
                user_fav.user = request.user
                user_fav.fav_id =int(fav_id)
                user_fav.fav_type=int(fav_type)
                user_fav.save()
                return HttpResponse({"status": "success", "msg": "已收藏"}, content_type='application/json')
            else:
                return HttpResponse({"status": "fail", "msg": "收藏出错"}, content_type='application/json')










