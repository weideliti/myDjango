# _*_ coding: utf-8 _*_
__author__ = 'weide'
__date__ = '2017/11/7 17:56'
import xadmin
from xadmin import views


from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    ebanle_themes = True
    use_bootswatch = True

class GlobaSetting(object):
    site_title = u"weide后台管理系统"
    site_footer = u"weide"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code','email','send_type','send_time'] #过滤器




class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title','image','url', 'index', 'add_time'] #过滤器


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobaSetting)