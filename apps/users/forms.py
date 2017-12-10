# _*_ coding: utf-8 _*_
__author__ = 'weide'
__date__ = '2017/11/14 18:35'
from django import forms
from captcha.fields import CaptchaField
#对输入的数据进行对错分析


class LoginForm(forms.Form):
    username = forms.CharField(required=True)  #定义名称必须和html中的一样
    password = forms.CharField(required=True,min_length=5)#最小长度是5


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})



class ModifyFrom(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)