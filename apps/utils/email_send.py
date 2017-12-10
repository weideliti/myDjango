# _*_ coding: utf-8 _*_
__author__ = 'weide'
__date__ = '2017/11/15 14:03'
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from random import Random
from three.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars ='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str+= chars[random.randint(0,length)]
    return str


def send_register_email(email,send_type=0):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_time
    email_record.send_type = send_type
    email_record.save()

    email_title=''
    email_body= ''
    if send_type=="register":
        # email_title="在线激活链接"
        # email_body = "点击下面链接激活账号：http://127.0.0.1/active/{0}".format(code)
        #
        # send_status=send_mail(email_title, email_body, EMAIL_FROM, [email])
        # if send_status:
            pass

    elif send_type=="forget":
        # email_title="在线找回密码链接"
        # email_body = "点击下面链接找回密码：http://127.0.0.1:8000"/reset/{0}".format(code)
        #
        # send_status=send_mail(email_title, email_body, EMAIL_FROM, [email])
        # if send_status:
        pass






