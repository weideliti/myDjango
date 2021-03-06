# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from organization.models import CourseOrg

# Create your models here.


class Course(models.Model):
    CourseOrg = models.ForeignKey(CourseOrg,verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(verbose_name=u"难度", max_length=2, choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")))
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长（分钟）")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y%m",verbose_name=u"封面")
    click_nums = models.IntegerField(verbose_name=u"点击量", default=0)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"课程名")
    name = models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"章节名")
    name = models.CharField(max_length=100,verbose_name=u"视频名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name=u"资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"课程资源"
        verbose_name_plural= verbose_name

